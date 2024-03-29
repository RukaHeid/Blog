# Generated by Django 5.0.1 on 2024-01-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="posts",
            field=models.ManyToManyField(
                blank=True, related_name="posts_under_tag", to="blogapp.post"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags_on_post", to="blogapp.tag"
            ),
        ),
    ]
