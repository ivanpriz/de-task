from environs import Env

env = Env()
env.read_env()


class Config:
    with env.prefixed("SQLSERVER_"):
        SQLSERVER_JAR_PATH = env("JAR_PATH")
        SQLSERVER_HOST = env("HOST")
        SQLSERVER_PORT = env.int("PORT")
        SQLSERVER_DB_NAME = env("DB_NAME")
        SQLSERVER_USER = env("USER")
        SQLSERVER_PASSWORD = env("PASSWORD")
        SQLSERVER_ADDITIONAL_PARAMS = env("ADDITIONAL_PARAMS", "encrypt=true;trustServerCertificate=true;")

    SQLSERVER_SPARK_JDBC_URI = f"jdbc:sqlserver://" \
                               f"{SQLSERVER_HOST}:{SQLSERVER_PORT};" \
                               f"databaseName={SQLSERVER_DB_NAME};" \
                               f"{SQLSERVER_ADDITIONAL_PARAMS}"
    SQLSERVER_CONNECTION_DETAILS = {
        "user": SQLSERVER_USER,
        "password": SQLSERVER_PASSWORD,
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
    }

    with env.prefixed("POSTGRES_"):
        POSTGRES_JAR_PATH = env("JAR_PATH")
        POSTGRES_HOST = env("HOST")
        POSTGRES_PORT = env.int("PORT")
        POSTGRES_USER = env("USER")
        POSTGRES_PASSWORD = env("PASSWORD")
        POSTGRES_DB = env("DB")

    POSTGRES_SPARK_JDBC_URI = f"jdbc:postgresql://{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
