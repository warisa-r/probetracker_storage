# Generated by Django 4.2.1 on 2023-06-06 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_metadata_metadataname_metadata_metadataunit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='metadataScheme',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='api.metadatascheme'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ItemMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='api.item')),
                ('metadata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metadata')),
            ],
        ),
    ]