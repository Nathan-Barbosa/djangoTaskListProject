# Generated by Django 4.0.3 on 2022-05-20 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskList.frame')),
            ],
        ),
    ]
