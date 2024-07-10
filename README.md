Book: Django 5 by Example (5th Edition)

# To Run
```
> py manage.py runserver

# run celery, open another terminal
> source env/myshop/bin/activate
> cd myshop
> celery -A myshop worker -l info

# open another terminal
# beside RabbitMQ management UI, use Flower to monitor celery
> source env/myshop/bin/activate
> cd myshop
> celery -A myshop flower
# http://localhost:5555

# Stripe webhook, open another terminal
> stripe login
> stripe listen --forward-to 127.0.0.1:8000/payment/webhook/

# collect all static file
> python manage.py collectstatic
```