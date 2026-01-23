# 1️⃣ Use official lightweight Python image
FROM python:3.13-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Install system dependencies (needed for mysql + cryptography)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ Copy dependency files first (layer caching)
COPY requirements.txt .

# 5️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Copy application code
COPY app ./app

# 7️⃣ Expose port
EXPOSE 8000

# 8️⃣ Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]