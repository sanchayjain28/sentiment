# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code and install dependencies
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn textblob

# Expose port
EXPOSE 8090

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]
