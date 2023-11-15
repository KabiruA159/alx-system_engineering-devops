description "Gunicorn application server running AirBnB_clone_v4"
author "Kabiru Abdullahi"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid ubuntu
setgid www-data

chdir /home/ubuntu/AirBnB_clone_v4

