# Generated by Django 4.2.1 on 2023-06-06 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_item_metadatascheme_itemmetadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='metadataScheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.metadatascheme'),
        ),
    ]
