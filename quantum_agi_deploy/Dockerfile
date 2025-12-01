FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    supervisor \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN mkdir -p /app/app/python_service /app/app/node_service /var/log/supervisor

# Install Dependencies
RUN pip install --no-cache-dir numpy

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY main.py /app/app/python_service/app.py

# Create dummy node service
RUN echo "console.log('Node Service Active'); setInterval(() => {}, 10000);" > /app/app/node_service/app.js

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
