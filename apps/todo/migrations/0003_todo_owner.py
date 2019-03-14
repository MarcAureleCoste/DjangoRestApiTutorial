# Generated by Django 2.1.7 on 2019-03-01 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todouser'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.TodoUser'),
            preserve_default=False,
        ),
    ]
