FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .

COPY src ./src

RUN pip install --no-cache-dir -e .

CMD ["python", "src/main.py"]