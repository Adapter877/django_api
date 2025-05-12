FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ติดตั้ง system packages ที่จำเป็นสำหรับ mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade setuptools wheel
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/
