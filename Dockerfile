FROM python:3.12.0a7-alpine3.18

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 443 for the Flask application
EXPOSE 443

# Set the Flask app environment variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=443
ENV FLASK_APP=backend.py

# Run the Flask application
CMD ["python3", "backend.py", "--host=0.0.0.0", "--port=443"]
