FROM python:3.12.0a7-alpine3.18

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 443 for the Flask application
EXPOSE 5000


# Run the Flask application
CMD ["python3", "backend.py"]
