# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (required for Playwright)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium

# Copy the application code
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Expose port (Railway will set this)
EXPOSE 8000

# Create a startup script
RUN echo '#!/bin/bash\n\
echo "🚀 Starting GlobalCouponFinder Scraping Service"\n\
echo "Working directory: $(pwd)"\n\
echo "Available files: $(ls -la)"\n\
echo "Changing to scrapers directory..."\n\
cd scrapers\n\
echo "New working directory: $(pwd)"\n\
echo "Available files in scrapers: $(ls -la)"\n\
if [ "$SERVICE_TYPE" = "beat" ]; then\n\
    echo "🕐 Starting Celery Beat Scheduler..."\n\
    celery -A celery_app beat --loglevel=info\n\
else\n\
    echo "👷 Starting Celery Worker..."\n\
    celery -A celery_app worker --loglevel=info --concurrency=5\n\
fi' > /app/start.sh && chmod +x /app/start.sh

# Start command
CMD ["/app/start.sh"]
