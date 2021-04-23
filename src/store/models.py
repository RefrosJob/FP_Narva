from django.db import models

# Create your models here.
class Product(models.Model): 

    # Default JSON Value
    def default_json():
        return {"attribute template" : "value"}

    # Primary key
    id = models.AutoField(primary_key=True)

    # Text Types
    title             = models.CharField(default='Template Title', max_length=120)
    description       = models.TextField(default='Template Description')
    descriptionShort  = models.TextField(default='Template Short Description')

    # Decimal Types
    price             = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    # Image Types

    imagePreview      = models.ImageField(default='img/small_def.png', upload_to='img/')
    imageMain         = models.ImageField(default='img/norm_def.png', upload_to='img/')

    # JSON Type

    attributes        = models.JSONField("Attributes", default=default_json, null=True, blank=True)

    # Foreign Keys

    subCathegoryFK         = models.ForeignKey('SubCathegory', on_delete=models.PROTECT, null=True, blank=True)

class Cathegory(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)

    # Text Types
    cathegoryName = models.CharField(default='Cathegory Template', max_length=40)
    
   
class SubCathegory(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)

    # Text Types
    subCathegoryName = models.CharField(default='Subcathegory Template', max_length=40)

     # Foreign Keys
    cathegoryFK = models.ForeignKey('Cathegory', on_delete=models.PROTECT)

class Attribute(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)

    # Text Types
    attributeName = models.CharField(default='Attribute Template', max_length=30)

    # Foreign Keys
    subCathegoryFK = models.ForeignKey('SubCathegory', on_delete=models.PROTECT)