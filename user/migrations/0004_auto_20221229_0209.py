# Generated by Django 3.0.8 on 2022-12-28 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20221229_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='kakao_token',
            new_name='username',
        ),
    ]
