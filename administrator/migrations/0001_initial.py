# Generated by Django 3.0.8 on 2020-11-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Names', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=30, null=True)),
                ('Profession', models.CharField(choices=[('Student', 'student'), ('Lecturer', 'Lecturer'), ('Security', 'Security'), ('Administrator', 'Administrator')], max_length=30, null=True)),
                ('Calling_hours', models.CharField(max_length=20, null=True)),
                ('Comments', models.TextField(max_length=200, null=True)),
                ('Date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Details', models.TextField(max_length=200, null=True)),
                ('DatePosted', models.DateTimeField(auto_now=True, null=True)),
                ('UserProfession', models.TextField(choices=[('Student', 'student'), ('Lecturer', 'Lecturer'), ('Security', 'Security'), ('Administrator', 'Administrator')], max_length=200, null=True)),
            ],
        ),
    ]
