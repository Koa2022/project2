# Generated by Django 4.2.2 on 2023-08-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_title_web_titlev_remove_web_data_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='category',
            field=models.IntegerField(choices=[(1, 'ข่าวประกาศ'), (2, 'โฆษณา'), (3, 'บันทึก')], default=1),
            preserve_default=False,
        ),
    ]
