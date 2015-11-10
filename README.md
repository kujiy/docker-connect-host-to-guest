
# Connect Docker HOST os to Docker Containers  
## (I mean) Connect Docker host OS to guest OS  
### docker-connect-host-to-guest

This tool allows you to connect your Docker host OS to Docker guest OS using container's name.  

If you execute this .py, then you can use this;
````bash
ping your-container-name
curl -s your-container-name
git clone git@your-container-name:you/project.git
````
You can access your container from your host os by container's name.

Add Docker container names and IPs into /etc/hosts of Docker Host OS

Update /etc/hosts of Docker Host OS to access its containers by container's name  
  
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
  
This tool adds container names and local IPs into your /etc/hosts/ Like this;  
  
````hosts  
172.17.0.147 gitlab  
172.17.0.135 redmine  
172.17.0.134 redmine-postgresql  
172.17.0.146 gitlab-postgresql  
172.17.0.145 gitlab-redis  
172.17.0.59 cent7_s  
172.17.0.58 cent6_s  
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
Reminds that you should set the tipical name to your docker containers.
You can see your running docker container names using this command below.

````bash  
[host_os]# docker ps --format "{{.Names}}"  
````

If you can't see your container name in that, check whether or not your "docker run" command has "-name" option.
````bash
docker run -d -name YOUR_CONTAINER_NAME imagename
````

I hope this helps you.  
Have fun.  
  
  
  
