# Generated by Django 5.0.4 on 2024-05-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_world_content_world_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]