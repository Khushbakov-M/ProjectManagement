# Generated by Django 4.2.11 on 2024-06-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_developer_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='created_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='developer',
            name='updated_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='subteam',
            name='created_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='subteam',
            name='updated_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.CharField(default='22-06-2024 05:45', max_length=20),
        ),
    ]
