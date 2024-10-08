# Generated by Django 5.0.6 on 2024-07-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciepeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sellrecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
