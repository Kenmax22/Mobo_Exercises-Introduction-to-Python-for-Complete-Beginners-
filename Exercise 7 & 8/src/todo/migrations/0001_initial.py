# Generated by Django 3.2.5 on 2021-07-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(verbose_name='created date')),
            ],
        ),
    ]
