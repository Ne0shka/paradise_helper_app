FROM python:3.13.3-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y clang lib{jpeg-turbo,webp}-dev python{,-dev} zlib-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -U setuptools && \
    pip install --no-cache-dir -r prod.txt && \
    rm -f prod.txt

COPY app/ app/

CMD ["python", "-m", "app"]