#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

content='
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
'
new_server='
location /hbnb_static {
alias /data/web_static/current/;
index index.html;
}
'
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "$content" >  /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
ssed -i "s|server_name _;|$new_server|" /etc/nginx/sites-available/default
