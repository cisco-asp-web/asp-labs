# Base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y sudo containerlab nginx

# Copy app
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip install flask

# Expose port
EXPOSE 8080

# Command to run both Nginx and Flask
CMD service nginx start && python app.py