# Generated by Django 4.2 on 2023-05-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texte',
            fields=[
                ('textfeld', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='text-Feld')),
                ('text', models.CharField(max_length=20, verbose_name='text')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texte',
            },
        ),
    ]
