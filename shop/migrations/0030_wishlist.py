# Generated by Django 4.1 on 2023-03-04 14:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_productview_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=1000, primary_key=True, serialize=False)),
                ('user_username', models.CharField(max_length=10000)),
                ('product_id', models.CharField(max_length=10000)),
            ],
        ),
    ]
