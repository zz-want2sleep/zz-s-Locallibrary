# Generated by Django 2.2.7 on 2019-11-19 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191119_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='choice_text',
        ),
    ]