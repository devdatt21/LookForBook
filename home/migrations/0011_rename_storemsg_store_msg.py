# Generated by Django 4.1 on 2023-02-10 14:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_storemsg_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='storeMsg',
            new_name='Store_Msg',
        ),
    ]
