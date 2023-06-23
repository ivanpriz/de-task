import logging
from typing import Optional

from pyspark.sql import SparkSession

from .config import Config
from .extractor import Extractor
from .loader import Loader
from .schemas import tables_schemas
from .utils import create_logger


class ETL:
    def __init__(self):
        self.logger = create_logger()

        self.spark: Optional[SparkSession] = None
        self.loader: Optional[Loader] = None
        self.extractor: Optional[Extractor] = None

    def build_spark(
            self,
            app_name: str,
            extra_class_paths: list[str],
            jars: list[str],
    ) -> SparkSession:
        """Creating Spark session. "spark.scheduler.mode", "FAIR" is required for parallelizing tasks."""
        self.logger.debug("Building spark session...")
        sp = SparkSession \
            .builder \
            .appName(app_name) \
            .config("spark.driver.extraClassPath", ";".join(extra_class_paths)) \
            .config("spark.jars", ",".join(jars)) \
            .config("spark.scheduler.mode", "FAIR") \
            .master("local") \
            .getOrCreate()
        self.logger.debug("Spark session created.")

        return sp

    def _on_start(self):
        self.logger.info("Starting app...")
        self.spark = self.build_spark(
            app_name="Loader",
            extra_class_paths=[
                "com.microsoft.sqlserver.jdbc.SQLServerDriver",
            ],
            jars=[
                Config.SQLSERVER_JAR_PATH,
                Config.POSTGRES_JAR_PATH,
            ],
        )
        self.extractor = Extractor(self.spark, self.logger)
        self.loader = Loader(self.logger)
        self.logger.info("App started!")

    def _etl_table(self, table_name: str):
        df = self.extractor.extract_source_table(table_name, tables_schemas[table_name])
        self.loader.save_postgres_table(df, table_name.lower())

    def _run(self):
        self.logger.info("Running ETL...")
        for table_name in tables_schemas:
            self._etl_table(table_name)
        self.logger.info("ETL finished!")

    def _on_shutdown(self):
        self.logger.info("Closing app...")
        self.logger.debug("Closing Spark session...")
        self.spark.stop()
        self.logger.debug("Session closed!")
        self.logger.info("App closed!")

    def start(self):
        self._on_start()
        self._run()
        self._on_shutdown()
