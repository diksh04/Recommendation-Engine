# Generated by Django 3.2 on 2022-05-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_delete_movierecommendationtagstable'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRecommendationTagsTable',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, max_length=255)),
                ('tags', models.TextField(max_length=2000, null=True)),
            ],
        ),
    ]
