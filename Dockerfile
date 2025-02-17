FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir flask treepoem

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
