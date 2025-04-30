FROM python:3.11-slim-bullseye

WORKDIR /app

# Устанавливаем netcat для ожидания БД
RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]



# CMD python manage.py migrate \
#     && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username="root").exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
#     && python manage.py loaddata fixtures/categories.json \
#     && python manage.py loaddata fixtures/products.json \
#     && python manage.py runserver 0.0.0.0:8000
