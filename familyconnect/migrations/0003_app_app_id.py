# Generated by Django 3.0.8 on 2020-07-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyconnect', '0002_auto_20200704_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='app_id',
            field=models.CharField(default='Empty', max_length=50),
            preserve_default=False,
        ),
    ]
