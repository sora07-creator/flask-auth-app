# --- Build Stage ---
FROM python:3.10-slim as builder

WORKDIR /install
COPY requirements.txt .
RUN pip install --prefix=/install/deps -r requirements.txt

# --- Final Stage ---
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /install/deps /usr/local
COPY . .

CMD ["python", "app.py"]
