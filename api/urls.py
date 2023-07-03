from django.urls import path
from .views import LocationList, LocationDetail, PhotoUploadView, PhotoView, MetadataSchemeList, MetadataSchemeDetail, MetadataList, MetadataDetail, ResearchSampleList, ResearchSampleDetail,ResearchSampleBySchemeList, SampleMetadataDetail, SampleMetadataList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('api/upload/', PhotoUploadView.as_view()),
    path('metadata/', MetadataList.as_view()),
    path('metadata/<int:pk>/', MetadataDetail.as_view()),
    path('metadata-schemes/', MetadataSchemeList.as_view()),
    path('metadata-schemes/<int:pk>/', MetadataSchemeDetail.as_view()),
    path('locations/', LocationList.as_view()),
    path('locations/<int:pk>/', LocationDetail.as_view()),
    path('research-samples/', ResearchSampleList.as_view()),
    path('research-samples/<int:pk>/', ResearchSampleDetail.as_view()),
    path('research-samples/scheme/<int:scheme_id>/', ResearchSampleBySchemeList.as_view()),
    path('sample-metadata/', SampleMetadataList.as_view()),
    path('sample-metadata/<int:scheme_id>/', SampleMetadataDetail.as_view()),
] 

