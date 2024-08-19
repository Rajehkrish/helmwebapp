FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py ./

EXPOSE 5000

CMD ["python", "app.py"]
