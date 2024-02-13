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
    cron \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a crontab file
RUN echo "* * * * * /usr/src/app/run_delete_expired_values_cron.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/delete_expired_values

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/delete_expired_values \
    && crontab /etc/cron.d/delete_expired_values

# Create the log file to be able to run tail and see cron job logs
RUN touch /var/log/cron.log

# Make port 8000 available to the world outside this container
EXPOSE 8000


ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

