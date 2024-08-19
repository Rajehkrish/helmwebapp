# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY flaskapp/requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY flaskapp/app.py ./

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
