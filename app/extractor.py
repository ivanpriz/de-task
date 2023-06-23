import logging

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType

from .config import Config
from .utils import preprocess_struct_schema_str


class Extractor:
    def __init__(self, spark: SparkSession, logger: logging.Logger):
        self.logger = logger
        self.spark = spark

    def extract_source_table(self, table_name: str, schema: StructType) -> DataFrame:
        props = Config.SQLSERVER_CONNECTION_DETAILS.copy()
        props.update(
            {
                "customSchema": preprocess_struct_schema_str(
                    schema.simpleString()
                )
            }
        )

        self.logger.debug("Extracting table %s from sqlserver...", table_name)

        res = self.spark.read.jdbc(
            url=Config.SQLSERVER_SPARK_JDBC_URI,
            table=table_name,
            properties=props,
        )

        self.logger.debug("Table %s extracted.", table_name)

        return res
