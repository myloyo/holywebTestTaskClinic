FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Сначала копируем только requirements.txt для кэширования
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-warn-script-location --upgrade pip && \
    pip install --no-warn-script-location -r requirements.txt

# Затем копируем весь остальной код
COPY . .

# Права на запись для SQLite
RUN chmod a+w /app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000 --noreload"]