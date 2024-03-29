# Generated by Django 4.2.1 on 2023-06-08 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_item_metadata_delete_itemmetadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('creator', models.CharField(blank=True, max_length=100)),
                ('subject_area', models.CharField(blank=True, max_length=100)),
                ('qrCode', models.ImageField(blank=True, upload_to='items/')),
            ],
        ),
        migrations.CreateModel(
            name='SampleMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.researchsample')),
            ],
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='metadataName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='metadataType',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='metadataUnit',
            new_name='unit',
        ),
        migrations.RenameField(
            model_name='metadatascheme',
            old_name='metadataSchemeCreator',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='metadatascheme',
            old_name='dateAdded',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='metadatascheme',
            old_name='metadataSchemeName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='locationName',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='metadataScheme',
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='scheme',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='api.metadatascheme'),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='samplescheme',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metadatascheme'),
        ),
        migrations.AddField(
            model_name='samplemetadata',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metadata'),
        ),
        migrations.AddField(
            model_name='samplemetadata',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.researchsample'),
        ),
        migrations.AddField(
            model_name='researchsample',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location'),
        ),
        migrations.AddField(
            model_name='researchsample',
            name='schemes',
            field=models.ManyToManyField(blank=True, related_name='samples', through='api.SampleScheme', to='api.metadatascheme'),
        ),
        migrations.AddField(
            model_name='metadata',
            name='samples',
            field=models.ManyToManyField(related_name='metadata', through='api.SampleMetadata', to='api.researchsample'),
        ),
    ]
