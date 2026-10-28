# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . ./

# Expose the default Flask port
EXPOSE 5000

# Set environment variables for production (optional)
ENV FLASK_ENV=production

# Run the Flask app
CMD ["python", "app.py"]

