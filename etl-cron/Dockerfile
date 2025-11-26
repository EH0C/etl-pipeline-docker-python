# Dockerfile
FROM python:3.11-alpine

# Install cron
RUN apk add --no-cache bash curl vim busybox-suid

# Set working directory
WORKDIR /app

# Copy your Python script
COPY script.py .

# Copy crontab file
COPY crontab /etc/crontabs/root

# Make sure cron logs to stdout so docker logs works
CMD ["crond", "-f", "-L", "/dev/stdout"]
