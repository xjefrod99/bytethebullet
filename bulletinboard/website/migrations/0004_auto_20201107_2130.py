# Generated by Django 3.0.7 on 2020-11-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201107_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='_person_contacts_+', to='website.Person'),
        ),
    ]
