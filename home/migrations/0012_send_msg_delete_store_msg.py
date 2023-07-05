# Generated by Django 4.1 on 2023-02-11 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_rename_storemsg_store_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('messagetext', models.TextField(blank=True, null=True)),
                ('messageDate', models.DateField(auto_now_add=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.book_deatails')),
                ('requestedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Store_Msg',
        ),
    ]
