FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY swagger_server/ /usr/src/app/swagger_server

#ENV MYSQL_HOST=mysql-service
#ENV MYSQL_PORT=3306
#ENV MYSQL_USER=username
#ARG MYSQL_PASSWORD
#ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}

#ENV MYSQL_DATABASE=lookup_db

EXPOSE 3000

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
