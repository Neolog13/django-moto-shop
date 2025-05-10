#!/bin/sh

set -e  # Остановить выполнение при ошибке

echo "⏳ Ожидаем доступность PostgreSQL..."
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    echo "Ждём $POSTGRES_HOST:$POSTGRES_PORT..."
    sleep 1
done

echo "🧩 Применяем миграции..."
python manage.py migrate

echo
python manage.py collectstatic --noinput

echo "👤 Создаём суперпользователя (если не существует)..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='root').exists():
    User.objects.create_superuser('root', 'root@example.com', 'root')
"

echo "📦 Загружаем фикстуры..."
python manage.py loaddata fixtures/categories.json || echo "⚠️ categories.json не найден"
python manage.py loaddata fixtures/products.json || echo "⚠️ products.json не найден"

echo "🚀 Запуск сервера..."
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000
# exec python manage.py runserver 0.0.0.0:8000