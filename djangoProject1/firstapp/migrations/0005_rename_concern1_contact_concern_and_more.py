# Generated by Django 4.2 on 2023-05-10 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_contact_concern1_contact_email1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='concern1',
            new_name='concern',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email1',
            new_name='email',
        ),
    ]