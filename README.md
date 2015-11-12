
# Connect Docker HOST os to Docker Containers Using container's names etc
## (I mean) Connect Docker host OS to guest OS by container names, domain names and hostnames of containers.
### docker-connect-host-to-guest

This tool allows you to connect your Docker host OS to Docker guest OS using
- container's name
- container's domain name
- container's hostname

If you execute this .py, then you can use this;
````bash
ping your-container-name
curl -s your-container-name
git clone git@your-container-name:you/project.git
````
You can access your container from your host os easily.

This tool adds and updates docker container parameters into /etc/hosts of Docker Host OS.
(This tool updates /etc/hosts of your Docker Host OS to access its containers by container's name.)

# Description

If you're runnning these docker containers;

````bash
[host_os]# docker ps --format "{{.Names}}"
gitlab
redmine
redmine-postgresql
gitlab-postgresql
gitlab-redis
cent7_s
cent6_s
````

This tool adds container names and local IPs into your /etc/hosts Like this;

````hosts
172.17.0.147 gitlab
172.17.0.135 redmine
172.17.0.134 redmine-postgresql
172.17.0.146 gitlab-postgresql
172.17.0.145 gitlab-redis
172.17.0.59 cent7_s
172.17.0.58 cent6_s
172.17.0.147 gitlab.exapmle.com
172.17.0.135 redmine.exapmle.com
172.17.0.134 redmine-postgresql.exapmle.com
172.17.0.146 gitlab-postgresql.exapmle.com
172.17.0.145 gitlab-redis.exapmle.com
172.17.0.59 cent7_s.exapmle.com
172.17.0.58 cent6_s.exapmle.com
````

# Installation

Before you use this, you have to install nodejs and npm.
Because it needs "hostile" npm module.

````bash
npm i hostile -g
````

Then you download this tool.
````bash
git clone https://github.com/kujiy/docker-connect-host-to-guest.git
````

# How to use
Just run. It doesn't need args.

````bash
python docker-connect-host-to-guest.py
````

# Note
1. This tool changes your /etc/hosts so that you should take a back up of the file first.
1. This tool won't allow your containers have duplicated hostname.  You should remove duplicated hostname on each container first.
1. Reminds that you should set the tipical name to your docker containers.
You can see your running docker container names using this command below.

````bash
[host_os]# docker ps --format "{{.Names}}"
````

If you can't see your container name in that, check whether or not your "docker run" command has "-name" option.
````bash
docker run -d -name YOUR_CONTAINER_NAME imagename
````

# History
### v0.1
Add container's name feature.
Now you can access to your containers using each container name.

### v0.2
Add container's domain name and hostname feature.
Now you can access to your containers using each container domain name or hostname.

***

I hope this helps you.
Have fun.



