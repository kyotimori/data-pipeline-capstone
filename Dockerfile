FROM python:3.11.15-slim-trixie

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir .

CMD ["pytest"]