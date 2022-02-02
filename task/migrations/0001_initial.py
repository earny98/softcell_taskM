# Generated by Django 4.0.2 on 2022-02-02 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(default=None, max_length=30)),
                ('group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.group')),
                ('project_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.user')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.group')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Incident_number', models.IntegerField()),
                ('issue_subject', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.user')),
                ('service_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.group')),
            ],
        ),
    ]
