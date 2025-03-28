# Generated by Django 4.2.11 on 2024-06-05 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(choices=[('jismoniy', 'Jismoniy shaxs'), ('yuiridik', 'Yuridik shaxs')], max_length=50)),
                ('project_name', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('cost', models.IntegerField()),
                ('tashkilot_nomi', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=700)),
                ('phone', models.CharField(help_text='+998 bilan kiriting!!!', max_length=15)),
                ('name_of_employer', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='documents')),
                ('file2', models.FileField(null=True, upload_to='documents')),
                ('file3', models.FileField(null=True, upload_to='documents')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('refused', 'Rad Etilgan'), ('pending', 'Kutilyapti'), ('accepted', 'Qabul qilingan')], default='pending', max_length=50)),
                ('deadline', models.DateField()),
                ('cost', models.IntegerField()),
                ('description', models.CharField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('announcement', models.ForeignKey(limit_choices_to={'assigned_to': None, 'deleted_at': None}, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='announcements.announcement')),
            ],
        ),
    ]
