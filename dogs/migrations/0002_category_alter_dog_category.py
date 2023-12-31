# Generated by Django 5.0 on 2023-12-14 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='порода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'порода',
                'verbose_name_plural': 'породы',
            },
        ),
        migrations.AlterField(
            model_name='dog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.category'),
        ),
    ]
