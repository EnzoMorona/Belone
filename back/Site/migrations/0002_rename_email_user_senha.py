# Generated by Django 4.2.2 on 2023-06-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='senha',
        ),
    ]