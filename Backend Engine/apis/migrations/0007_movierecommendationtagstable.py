# Generated by Django 3.2 on 2022-05-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_delete_movierecommendationtagstable'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRecommendationTagsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.TextField(blank=True, max_length=255)),
                ('tags', models.TextField(max_length=2000, null=True)),
            ],
        ),
    ]
