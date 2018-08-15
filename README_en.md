# docker-django-mysql-celery
docker-compose project with mysql as db, redis as cache, django as web, celery as task queue, haproxy as load balance tool

## Dependencies

> Docker, Docker Compose

## How to start

### clone project

```
git clone https://github.com/aishenghuomeidaoli/docker-django-mysql-celery.git

cd docker-django-mysql-celery
```

### init mysql

This will create a mysql database.

If you have a mysql server outside host machine, ignore this and change django settings to your mysql endpoint.

```
docker-compose -f docker-compose-mysql.yaml up -d

mysql -u root -h 0.0.0.0 -p

mysql> CREATE DATABASE mydb CHARACTER SET utf8 COLLATE utf8_general_ci;
```

### start project

This will create/recreate mysql container, create web container, redis container, haproxy container

```
docker-compose up -d

```

Load balance is available with `--scale` option.

This will create 2 web containers.

```
docker-compose up -d --scale web=2
```

