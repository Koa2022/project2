# Generated by Django 4.2.2 on 2023-08-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='web',
            old_name='title',
            new_name='titlev',
        ),
        migrations.RemoveField(
            model_name='web',
            name='data_created',
        ),
        migrations.AddField(
            model_name='web',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]