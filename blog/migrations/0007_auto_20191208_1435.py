# Generated by Django 2.2 on 2019-12-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191208_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='browse_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='goods',
            name='praise_count',
            field=models.IntegerField(default=1),
        ),
    ]
