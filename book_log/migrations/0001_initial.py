# Generated by Django 5.2.3 on 2025-06-19 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('author', models.TextField(blank=True, default='', max_length=50)),
                ('startDate', models.DateTimeField(default=datetime.datetime(2025, 6, 19, 17, 10, 19, 882993, tzinfo=datetime.timezone.utc))),
                ('rating', models.IntegerField(default=1, max_length=1)),
                ('status', models.TextField(choices=[('LENDO', 'lendo'), ('CONCLUIDO', 'concluido'), ('PAUSADO', 'pausado'), ('ABANDONADO', 'abandonado')], max_length=10)),
            ],
        ),
    ]
