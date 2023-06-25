#Dockerfile for the flask application
# Use the Alpine Linux as the base image
FROM python:3.9-alpine

# Install required packages
RUN apk update && \
    apk add --no-cache mysql-dev build-base && \
    pip install flask-mysqldb
# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /app

# Set environment variables
ENV FLASK_APP=app.py
ENV MYSQL_DATABASE=votes
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password
ENV MYSQL_HOST=mysql
# Expose the port used by the Flask application
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
