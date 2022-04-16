# Generated by Django 4.0.4 on 2022-04-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('text', models.CharField(max_length=200)),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
    ]
