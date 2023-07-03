from rest_framework import serializers
from .models import ResearchSample, Location, Metadata, MetadataScheme, SampleMetadata, SampleScheme


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = "__all__"


from rest_framework import serializers
from .models import SampleMetadata

class SampleMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleMetadata
        fields = "__all__"


class MetadataSchemeSerializer(serializers.ModelSerializer):
    metadata_attributes = MetadataSerializer(many=True, read_only=True)

    class Meta:
        model = MetadataScheme
        fields = ['id', 'name', 'creator', 'metadata_attributes']


class ResearchSampleSerializer(serializers.ModelSerializer):
    scheme = serializers.PrimaryKeyRelatedField(queryset=MetadataScheme.objects.all(), allow_null=True, required=False)
    metadata = SampleMetadataSerializer(source='samplemetadata_set', many=True, required=False)

    class Meta:
        model = ResearchSample
        fields = ['id', 'unique_id', 'date_added', 'title', 'creator', 'subject_area', 'location', 'qrCode', 'scheme', 'metadata']

    


class SampleSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleScheme
        fields = ['scheme']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']
