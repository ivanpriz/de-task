import logging

from pyspark.sql import DataFrame

from .config import Config


class Loader:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def save_postgres_table(self, df: DataFrame, table_name: str):
        self.logger.debug("Saving table %s...", table_name)

        df.write.format("jdbc") \
            .option("url", Config.POSTGRES_SPARK_JDBC_URI) \
            .option("driver", "org.postgresql.Driver") \
            .option("dbtable", table_name) \
            .option("user", Config.POSTGRES_USER) \
            .option("password", Config.POSTGRES_PASSWORD) \
            .mode("append") \
            .save()

        self.logger.debug("Table %s saved to local postgres.", table_name)
