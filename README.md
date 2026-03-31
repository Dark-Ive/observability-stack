# Observability Stack

A beginner friendly monitoring stack built with Docker Compose on Debian.

## Stack
- **Prometheus** - metrics collection
- **Grafana** - visualization & dashboards
- **Node Exporter** - system metrics
- **Alertmanager** - alert routing
- **Custom Python Exporter** - application-level metrics

## Setup
```bash
docker compose up -d
```

## Access
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Alertmanager: http://localhost:9093
