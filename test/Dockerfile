# Use official Python image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Copy app
COPY main.py .

# Expose port
EXPOSE 5000

# Run app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]