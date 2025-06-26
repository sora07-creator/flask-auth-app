# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask flask-bcrypt

# Run the app
CMD ["python", "app.py"]
