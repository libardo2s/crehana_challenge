FROM python:3.9-slim

# Create a non-root user and set up permissions
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies as root
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files with correct ownership
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser