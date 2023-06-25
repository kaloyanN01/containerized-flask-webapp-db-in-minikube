#Dockerfile for the MySQL datbase
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=votes
ENV MYSQL_PASSWORD=password
ENV MYSQL_HOST=mysql

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
