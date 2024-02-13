# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    cron \  # Add cron to the list of packages to install
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Ensure the script is executable
RUN chmod +x ./scripts/delete_expired_values.py

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Setup cron job
# Create a crontab file
RUN echo "* * * * * cd /usr/src/app && python ./scripts/delete_expired_values.py >> /var/log/cron.log 2>&1" > /etc/cron.d/delete_expired_values_cron
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/delete_expired_values_cron
# Apply cron job
RUN crontab /etc/cron.d/delete_expired_values_cron
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Start cron and Django application
CMD cron && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
