# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install them
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY app/ .

# Run the application
CMD ["python", "app.py"]