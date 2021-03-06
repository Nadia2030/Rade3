# Generated by Django 3.1.6 on 2021-02-19 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('url', models.URLField()),
                ('source', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Victim_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('program', models.TextField()),
                ('files', models.ImageField(null=True, upload_to='')),
                ('blackmailer_name', models.CharField(max_length=200)),
                ('blackmailer_email', models.EmailField(max_length=254)),
                ('blackmailer_account', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Victim_Request_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('contact_blackmailer', models.BooleanField(default=False)),
                ('timeـout', models.BooleanField(default=False)),
                ('results', models.TextField(null=True)),
                ('victim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Rade3App.victim_request')),
            ],
        ),
    ]
