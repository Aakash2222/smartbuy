# Generated by Django 4.0.2 on 2022-07-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andaman &Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andra Pradesh'), ('Bihar', 'Bihar'), ('UP', 'UP')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Andaman &Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andra Pradesh'), ('Bihar', 'Bihar'), ('UP', 'UP')], default='Pending', max_length=50),
        ),
    ]
