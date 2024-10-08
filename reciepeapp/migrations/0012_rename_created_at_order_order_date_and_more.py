# Generated by Django 5.0.7 on 2024-08-06 19:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reciepeapp", "0011_remove_cartitem_quantity_alter_recipe_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="created_at",
            new_name="order_date",
        ),
        migrations.RemoveField(
            model_name="order",
            name="payment_id",
        ),
        migrations.RemoveField(
            model_name="order",
            name="product_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total_amount",
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_address",
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="order_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Shipped", "Shipped"),
                    ("Delivered", "Delivered"),
                ],
                default="Pending",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="OrderedProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reciepeapp.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reciepeapp.recipe",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_id", models.CharField(max_length=255)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("Success", "Success"), ("Failed", "Failed")],
                        max_length=50,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reciepeapp.order",
                    ),
                ),
            ],
        ),
    ]
