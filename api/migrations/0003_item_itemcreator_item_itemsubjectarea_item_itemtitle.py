# Generated by Django 4.2.1 on 2023-06-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemCreator',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='itemSubjectArea',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='itemTitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
