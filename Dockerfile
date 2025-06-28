FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flask flask-bcrypt psycopg2-binary
CMD ["python", "app.py"]
