# Generated by Django 2.2.12 on 2020-05-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=256, null=True, verbose_name='个人形象'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='2000-1-1', verbose_name='出生日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=8, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=128, null=True, verbose_name='常居地'),
        ),
    ]
