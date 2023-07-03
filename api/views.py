from rest_framework import generics
from rest_framework.renderers import BrowsableAPIRenderer

from .models import Metadata, MetadataScheme, Location, ResearchSample, SampleMetadata
from .serializers import MetadataSerializer, MetadataSchemeSerializer, LocationSerializer, ResearchSampleSerializer, SampleMetadataSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.views.generic import View
from django.http import HttpResponseNotFound
from django.conf import settings
import os
from django.views import View
from django.http import HttpResponseNotFound

class MetadataList(generics.ListCreateAPIView):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()
    

class MetadataDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()
    

class MetadataSchemeList(generics.ListCreateAPIView):
    serializer_class = MetadataSchemeSerializer
    queryset = MetadataScheme.objects.all()
    

class MetadataSchemeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MetadataSchemeSerializer
    queryset = MetadataScheme.objects.all()
    

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    

class ResearchSampleList(generics.ListCreateAPIView):
    serializer_class = ResearchSampleSerializer
    queryset = ResearchSample.objects.all()
    

class ResearchSampleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResearchSampleSerializer
    queryset = ResearchSample.objects.all()
    

class ResearchSampleBySchemeList(generics.ListAPIView):
    serializer_class = ResearchSampleSerializer
    

    def get_queryset(self):
        scheme_id = self.kwargs['scheme_id']
        return ResearchSample.objects.filter(schemes__id=scheme_id)

class PhotoView(View):
    def get(self, request, *args, **kwargs):
        filename = kwargs['filename']
        photo_path = os.path.join(settings.MEDIA_ROOT, 'item', filename)

        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo_file:
                return HttpResponse(photo_file.read(), content_type='image/jpeg')
        else:
            return HttpResponseNotFound()

class PhotoUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = ResearchSample(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the item with the uploaded photo
            return Response({'message': 'Item uploaded successfully'}, status=201)
        return Response(serializer.errors, status=400)
    
class SampleMetadataList(generics.ListCreateAPIView):
    serializer_class = SampleMetadataSerializer
    queryset = SampleMetadata.objects.all()
    

class SampleMetadataDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SampleMetadataSerializer
    queryset = SampleMetadata.objects.all()