FROM python:3.9-slim

# Create a non-root user and set up permissions
RUN useradd -m appuser && \
    mkdir -p /app/static && \
    chown -R appuser:appuser /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV STATIC_ROOT /app/static

# Set work directory
WORKDIR /app

# Install dependencies as root
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files with correct ownership
COPY --chown=appuser:appuser . .

# Collect static files (run as root temporarily)
USER root
RUN python manage.py collectstatic --noinput
USER appuser
