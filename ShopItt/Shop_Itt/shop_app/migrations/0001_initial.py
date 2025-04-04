# Generated by Django 5.2 on 2025-04-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='img')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(blank=True, choices=[('Electronics', 'ELECTRONICS'), ('Groceries', 'GROCERIES'), ('Clothings', 'CLOTHINGS')], max_length=15, null=True)),
            ],
        ),
    ]
