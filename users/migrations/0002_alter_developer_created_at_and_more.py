# Generated by Django 4.2.11 on 2024-06-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='created_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='developer',
            name='updated_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='subteam',
            name='created_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='subteam',
            name='updated_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.CharField(default='11-06-2024 05:44', max_length=20),
        ),
    ]
