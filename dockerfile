# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    TELEGRAM_BOT_TOKEN="your_telegram_bot_token" \
    GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service_account.json"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        gcc \
        libffi-dev \
        libssl-dev \
        python3-dev \
        build-essential \
        curl \
        wget \
        unzip \
        apt-utils \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and dependencies
RUN pip install --upgrade pip \
    && pip install python-telegram-bot \
    && pip install google-cloud-translate

# Copy the bot script into the Docker image
COPY translate_bot.py /app/translate_bot.py

# Set the working directory
WORKDIR /app

# Run the bot script
CMD ["python", "translate_bot.py"]
