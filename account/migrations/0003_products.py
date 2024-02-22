# Generated by Django 4.0.6 on 2024-02-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
            ],
        ),
    ]