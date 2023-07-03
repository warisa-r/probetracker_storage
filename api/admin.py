from django.contrib import admin
from .models import Location, Metadata, MetadataScheme, ResearchSample, SampleMetadata
# Register your models here.

admin.site.register(ResearchSample)
admin.site.register(Location)
admin.site.register(MetadataScheme)
admin.site.register(Metadata)
admin.site.register(SampleMetadata)