FROM mysql:latest


# 创建数据库和用户，根据需要进行更改
#ENV MYSQL_DATABASE=lookup_db
#ENV MYSQL_USER=username
#ARG MYSQL_PASSWORD
#ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}


# 将数据库初始化脚本复制到容器内的初始化目录
COPY ./mysql/init.sql /docker-entrypoint-initdb.d/

# 暴露MySQL的默认端口
EXPOSE 3306
