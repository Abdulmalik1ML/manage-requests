# Generated by Django 4.2.5 on 2023-10-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='Pending', max_length=300),
        ),
    ]