# docker-django-mysql-celery
docker-compose project with mysql as db, redis as cache, django as web, celery as task queue, haproxy as load balance tool

[English Doc](./README_en.md)

## 依赖

> Docker, Docker Compose

## 如何开始

### 克隆项目

```
git clone https://github.com/aishenghuomeidaoli/docker-django-mysql-celery.git

cd docker-django-mysql-celery
```

### 初始化MySQL

这里会创建一个`MySQL`数据库，方便`Django`服务端连接。

如果你有一个远程的`MySQL`服务器，请跳过此处，在[Django配置文件中](./web/web/settings.py)修改数据库地址。

[查看容器化MySQL的原因](https://aishenghuomeidaoli.github.io/%E6%8A%80%E6%9C%AF/%E6%8E%A2%E7%B4%A2docker%E5%AE%B9%E5%99%A8%E4%B8%8Bmysql%E7%9A%84%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96/)

```
docker-compose -f docker-compose-mysql.yaml up -d

mysql -u root -h 0.0.0.0 -p
```

执行SQL，创建数据库，修改时区。

```
CREATE DATABASE mydb CHARACTER SET utf8 COLLATE utf8_general_ci;
SET time_zone = 'Asia/Shanghai';
```

### 启动项目

这里会为 mysql、web、redis、haproxy创建容器。

```
docker-compose up -d

```

因为`Haproxy`的存在，可以开启多个web容器，支持负载均衡。

```
docker-compose up -d --scale web=2
```

### 访问页面

打开浏览器，访问 http://0.0.0.0/ ，创建一个运算任务、任务执行结束后，页面会刷新任务列表