FROM python:3.13.3-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y clang libjpeg62-turbo-dev libwebp-dev python3-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -U setuptools && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

COPY app/ app/

CMD ["python", "-m", "app"]