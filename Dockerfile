FROM python:3.13-slim
WORKDIR /app
RUN pip install prometheus-client psutil
COPY custom_exporter.py .
CMD ["python3", "custom_exporter.py"]
