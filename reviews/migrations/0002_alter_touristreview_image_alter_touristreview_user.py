# Generated by Django 5.0.2 on 2024-02-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristreview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/review_images/'),
        ),
        migrations.AlterField(
            model_name='touristreview',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
