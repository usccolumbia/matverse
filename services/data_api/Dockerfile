FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && useradd -u 1000 -m service
COPY data_api ./data_api
COPY static ./static
USER 1000:1000
CMD ["uvicorn", "data_api.api:app", "--host", "0.0.0.0", "--port", "8094", "--proxy-headers", "--forwarded-allow-ips", "*"]
