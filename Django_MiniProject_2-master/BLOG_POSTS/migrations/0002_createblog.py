# Generated by Django 2.1.5 on 2020-06-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_POSTS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='createblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
