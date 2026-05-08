# Stage 1: Build the React Frontend
FROM node:18-alpine as build-stage
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Package the Final Application
FROM python:3.11-slim
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Copy the built frontend from the first stage
COPY --from=build-stage /app/frontend/dist /app/frontend/dist

# Expose the port (Render will override this with its own port)
EXPOSE 8000

# Start the application
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
