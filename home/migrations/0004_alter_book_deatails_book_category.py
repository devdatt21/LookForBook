# Generated by Django 4.1 on 2022-08-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_sendrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_deatails',
            name='book_category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
