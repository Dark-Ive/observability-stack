from prometheus_client import start_http_server, Gauge
import psutil
import time

# Define metrics
cpu_usage = Gauge('custom_cpu_usage_percent', 'CPU usage in percent')
memory_usage = Gauge('custom_memory_usage_percent', 'Memory usage in percent')
disk_usage = Gauge('custom_disk_usage_percent', 'Disk usage in percent')

def collect_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage('/').percent)

if __name__ == '__main__':
    start_http_server(8000)  # expose metrics on port 8000
    print("Custom exporter running on port 8000...")
    while True:
        collect_metrics()
        time.sleep(5)
