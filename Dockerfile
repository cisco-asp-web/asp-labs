# Use the official NGINX base image
FROM nginx

# Copy the static content to the container
COPY css /usr/share/nginx/html/css
COPY img /usr/share/nginx/html/img
COPY index.htm /usr/share/nginx/html/
COPY home.htm /usr/share/nginx/html/

# Expose the default HTTP port
EXPOSE 80

# Start NGINX when the container starts
CMD ["nginx", "-g", "daemon off;"]