# Generated by Django 3.1.2 on 2020-12-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipediaPost', '0003_post_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/slug'),
        ),
    ]
