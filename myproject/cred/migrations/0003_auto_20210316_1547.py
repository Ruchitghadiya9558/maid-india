# Generated by Django 3.1.7 on 2021-03-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cred', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
