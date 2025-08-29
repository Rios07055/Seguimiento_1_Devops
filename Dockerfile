# Dockerfile (simplificado y optimizado)
FROM python:3.11-slim

WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libffi-dev python3-dev cargo \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -r /src/requirements.txt

COPY . /src

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
