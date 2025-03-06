import random
from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import Category, Product
from django.utils.text import slugify
import urllib.request
import os
from django.core.files import File

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake categories and products with images'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Deleting old data...'))
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating fake categories...'))
        categories = []
        for _ in range(5):
            name = fake.word().capitalize()
            slug = slugify(name)
            category = Category.objects.create(name=name, slug=slug)
            categories.append(category)

        self.stdout.write(self.style.SUCCESS('Creating fake products...'))
        for _ in range(20):
            category = random.choice(categories)
            name = fake.sentence(nb_words=3).replace(".", "")
            slug = slugify(name)
            description = fake.paragraph(nb_sentences=5)
            price = round(random.uniform(10, 500), 2)
            available = random.choice([True, False])

            # Download a random image from Lorem Picsum
            image_url = f"https://picsum.photos/300/300?random={random.randint(1, 1000)}"
            image_name = f"product_{random.randint(1, 10000)}.jpg"
            image_path = f"media/products/{image_name}"

            # Save image locally
            urllib.request.urlretrieve(image_url, image_path)

            product = Product(
                category=category,
                name=name,
                slug=slug,
                description=description,
                price=price,
                available=available
            )

            # Attach the image to the product
            with open(image_path, 'rb') as img_file:
                product.image.save(image_name, File(img_file), save=True)

        self.stdout.write(self.style.SUCCESS('Fake data with images generated successfully!'))
