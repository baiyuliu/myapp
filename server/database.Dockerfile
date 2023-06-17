FROM mysql:latest

# 设置root用户的密码，根据需要进行更改
ENV MYSQL_ROOT_PASSWORD=password

# 创建数据库和用户，根据需要进行更改
ENV MYSQL_DATABASE=lookup_db
ENV MYSQL_USER=username
ENV MYSQL_PASSWORD=password

# 将数据库初始化脚本复制到容器内的初始化目录
COPY ./mysql/init.sql /docker-entrypoint-initdb.d/

# 暴露MySQL的默认端口
EXPOSE 3306
