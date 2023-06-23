ETL to load data from MS SQL server to PostgreSQL with PySpark.

To start run:
```docker-compose up```

It will start postgres container, then start the migrations script.
After you will be able to access the data in the postgres.

You have to specify environment variables in `.env` file:

- SQLSERVER_HOST: remote sql server host
- SQLSERVER_PORT: remote sql server port
- SQLSERVER_DB_NAME: db name
- SQLSERVER_USER: db user
- SQLSERVER_PASSWORD: db password

Path to jars for JDBC.
Ideally it should be downloaded from some internal server in CI/CD pipeline,
but as for now for simplicity they are distributed inside repo.
- SQLSERVER_JAR_PATH=jars/sqljdbc_12.2/enu/mssql-jdbc-12.2.0.jre8.jar
- POSTGRES_JAR_PATH=jars/postgresql-42.6.0.jar

Local database with data is accessible at `postgres:postgres@localhost:5432`