# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY app ./app
COPY model.pkl .
COPY vectorizer.pkl .

# Expose port (optional, for documentation)
EXPOSE 10000

# Run FastAPI server using Render's PORT
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}"]