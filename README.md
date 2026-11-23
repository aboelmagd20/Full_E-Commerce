# Full E-Commerce (Django)

A Django online shop: product catalog, shopping cart, coupons, orders, and Stripe checkout. Learning project built while following a Django course.

## Features
- Product catalog with categories, product pages and images
- Session-based shopping cart (add / remove items)
- Coupon codes with validity dates and percentage discounts
- Order creation and an order record with a Stripe payment id
- Stripe Checkout payment flow with a webhook handler (`payment` app)
- PDF invoice generation with WeasyPrint (Celery task on payment)
- Celery task that runs when an order is created (`orders/tasks.py`)
- Product recommendations stored in Redis (`shop/recommender.py`)
- Admin order detail page with PDF export

## Tech stack
Python, Django, Celery, Redis, Stripe, WeasyPrint, SQLite (local), Django templates

## Run locally
```bash
python -m venv venv && source venv/bin/activate
pip install django celery redis stripe pillow weasyprint
cp .env.example .env     # then export these values in your shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Settings read secrets from environment variables (see `.env.example`). Redis must be running on localhost:6379 for recommendations and Celery.

## Structure
`shop/` catalog, `cart/`, `coupons/`, `orders/`, `payment/`, `myshop/` project settings.
