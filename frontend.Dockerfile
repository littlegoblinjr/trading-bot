FROM node:20-slim

WORKDIR /app

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest
COPY frontend/ .

# Expose Vite port
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
