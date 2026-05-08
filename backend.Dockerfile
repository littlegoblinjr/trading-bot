FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn python-dotenv python-binance

# Copy the rest of the code
COPY . .

# Expose port
EXPOSE 8000

CMD ["python", "app.py"]
