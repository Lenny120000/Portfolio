# Generated by Django 5.0.3 on 2024-03-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nimi', models.TextField(default='')),
                ('hinta', models.FloatField(default=0)),
                ('kuvaus', models.TextField(default='')),
                ('tuotekuva', models.FileField(default='', upload_to='snippets/uploads/')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]