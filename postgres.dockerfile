FROM postgres:15.1-alpine

COPY /initdb_scripts/*.sql /docker-entrypoint-initdb.d/
