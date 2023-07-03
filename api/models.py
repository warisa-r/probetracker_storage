from django.db import models

class MetadataScheme(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    creator = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class Metadata(models.Model):
    name = models.CharField(max_length=250, blank=True)
    unit = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=50, blank=True)
    #scheme = models.ForeignKey(MetadataScheme, on_delete=models.CASCADE, blank=True, default=1)
    scheme = models.ForeignKey(MetadataScheme, on_delete=models.CASCADE, related_name='metadata_attributes', blank=True, null = True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

class ResearchSample(models.Model):
    unique_id = models.CharField(max_length=50, blank= True)
    date_added = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    creator = models.CharField(max_length=100, blank=True)
    subject_area = models.CharField(max_length=100, blank=True)
    qrCode = models.ImageField(upload_to='items/', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    #schemes = models.ManyToManyField(MetadataScheme, related_name='samples', blank=True, through='SampleScheme')
    scheme = models.ForeignKey(MetadataScheme, on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return self.unique_id
    
class SampleScheme(models.Model):
    sample = models.ForeignKey(ResearchSample, on_delete=models.CASCADE)
    scheme = models.ForeignKey(MetadataScheme, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

class SampleMetadata(models.Model):
    sample = models.ForeignKey(ResearchSample, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    unit = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=100, blank=True)
    


