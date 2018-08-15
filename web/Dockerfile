FROM ubuntu:18.04

RUN apt-get update
RUN set_tz Asia/Shanghai
ENV TZ=Asia/Shanghai
RUN apt-get install apt-utils python3 python3-pip cron vim libmysqlclient-dev tzdata -y
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip3 install celery==4.2.0 Django==2.1 django-celery-results==1.0.1 django-redis-cache==1.7.1 ipython=6.5 mysqlclient==1.3.7 redis==2.10.5 uwsgi==2.0.15
