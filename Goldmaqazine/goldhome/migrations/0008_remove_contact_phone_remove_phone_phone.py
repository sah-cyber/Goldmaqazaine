# Generated by Django 4.1.1 on 2022-11-02 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldhome', '0007_alter_tag_options_alter_gold_post_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='phone',
        ),
    ]
