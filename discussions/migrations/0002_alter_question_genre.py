# Generated by Django 4.2.2 on 2023-07-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='genre',
            field=models.CharField(choices=[('A', 'agriculture'), ('F', 'Farm'), ('O', 'Organic'), ('S', 'Soil'), ('P', 'Pest'), ('S', 'Study'), ('N', 'Animals')], max_length=1),
        ),
    ]