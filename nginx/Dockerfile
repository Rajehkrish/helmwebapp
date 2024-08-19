FROM nginx:latest

# Copy Nginx configuration file
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy index.html to the Nginx web root
COPY nginx/index.html /usr/share/nginx/html/index.html

EXPOSE 80
