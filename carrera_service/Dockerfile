FROM python:3.11-slim
WORKDIR /app

COPY carrera_service/ ./carrera_service
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libffi-dev python3-dev cargo \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8000
EXPOSE 8000
CMD ["uvicorn", "carrera_service.main:app", "--host", "0.0.0.0", "--port", "8000"]

