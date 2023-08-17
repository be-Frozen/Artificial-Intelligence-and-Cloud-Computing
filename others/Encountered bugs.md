# Debugs

#### Can't import docker

`systemctl status docker`

check status you may see something like this:

![image-20230816113051431](docker.assets/image-20230816113051431.png)

`systemctl start docker`

you will fail EVERYTIME

![image-20230816113139137](docker.assets/image-20230816113139137.png)

`sudo apt install docker.io`

`sudo dockerd --debug`

`systemctl stop docker`

then restart, it will work.

**DON'T DO**

`sudo rm -rf /var/run/docker.pid` 

This will uninstall Docker Desktop on your computer.



#### docker ps

Cannot connect to the Docker daemon at unix:///home/befrozen/.docker/desktop/docker.sock. Is the docker daemon running?

check if you have installed docker desktop