# Generated by Django 2.1.5 on 2020-06-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_POSTS', '0002_createblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='createblog',
            name='Name',
            field=models.CharField(default='adi', max_length=30),
            preserve_default=False,
        ),
    ]