# Generated by Django 3.0 on 2020-01-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tower_app', '0006_auto_20200110_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='hp',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='roomID',
            field=models.IntegerField(default=26),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='strength',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='Room b', max_length=64),
        ),
        migrations.AlterField(
            model_name='player',
            name='strength',
            field=models.IntegerField(default=2),
        ),
    ]
