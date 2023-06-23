import logging


def preprocess_struct_schema_str(schema_str: str):
    """Formats StructType .simpleString method output to JDBC format."""
    return schema_str\
        .strip("struct<")\
        .strip(">")\
        .replace("int", "INT")\
        .replace("string", "STRING")\
        .replace(",", ", ")\
        .replace(":", " ")


def create_logger():
    logger = logging.getLogger('ETL')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    return logger
