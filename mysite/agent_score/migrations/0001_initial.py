# Generated by Django 2.1.1 on 2018-10-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(max_length=20)),
                ('observe_score', models.CharField(max_length=100)),
                ('evaluate_score', models.CharField(max_length=100)),
                ('predict_score', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'agent_score',
            },
        ),
    ]
