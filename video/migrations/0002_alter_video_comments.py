# Generated by Django 4.0.3 on 2022-03-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='comments',
            field=models.ManyToManyField(blank=True, to='video.comment'),
        ),
    ]