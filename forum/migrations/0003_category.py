# Generated by Django 5.1.3 on 2024-12-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_post_comment_psot_id_alter_dislike_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]