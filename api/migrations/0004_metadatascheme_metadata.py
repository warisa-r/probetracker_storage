# Generated by Django 4.2.1 on 2023-06-05 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_itemcreator_item_itemsubjectarea_item_itemtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetadataScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadataSchemeName', models.CharField(max_length=250, unique=True)),
                ('dateAdded', models.DateField(auto_now_add=True)),
                ('metadataSchemeCreator', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadataType', models.CharField(max_length=50)),
                ('metadataScheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metadatascheme')),
            ],
        ),
    ]
