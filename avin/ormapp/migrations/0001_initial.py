# Generated by Django 5.1.2 on 2024-10-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('accountno', models.IntegerField(primary_key='accountno', serialize=False)),
                ('loantype', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=60)),
                ('aadharno', models.IntegerField()),
            ],
        ),
    ]
