# Dockerfile
FROM python:3.11-alpine

# Install cron and bash utilities
RUN apk add --no-cache bash curl vim busybox-suid

# Set working directory
WORKDIR /app

# Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script
COPY script.py .

# Copy crontab file
COPY crontab /etc/crontabs/root

# Run cron in foreground so logs show in docker logs
CMD ["crond", "-f", "-L", "/dev/stdout"]
