# Generated by Django 3.1 on 2020-08-06 06:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, validators=[blog.models.min_length_3_validator]),
        ),
    ]
