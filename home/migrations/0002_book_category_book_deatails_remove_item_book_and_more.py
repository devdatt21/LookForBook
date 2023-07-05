# Generated by Django 4.0.6 on 2022-08-27 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.CharField(max_length=10, null=True)),
                ('category_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Deatails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(blank=True, max_length=200, null=True)),
                ('book_author', models.CharField(blank=True, max_length=200, null=True)),
                ('book_language', models.CharField(blank=True, max_length=200, null=True)),
                ('book_des', models.TextField(blank=True, null=True)),
                ('book_img', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('book_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.book_category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='book',
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
