from django.db import models
from django.utils import timezone
import os
from django.urls import reverse
# Create your models here.
# def upload_to_path(instance,filename):
#     return os.path.join(
#         ""
#     )
# BASE_DIR = Path(__file__).resolve().parent.parent    


def file_path(request,filename):
    old_filename = filename
    timenow = timezone.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timenow,old_filename)
    return os.path.join('static/images/shoes/shoes_DB/',filename)
    
    


class Shoe(models.Model):
    
    shoe_id = models.CharField(max_length=50,primary_key=True,default="SID0001")
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100,default="shoes model",null=False,blank=False)
    price = models.CharField(max_length=50,null=False,blank=False,default="0.0")
    category = models.CharField(max_length=50,default="sports shoes",null=False,blank=False)
    rating  = models.IntegerField(null=False,blank=False,default="5")
    color = models.CharField(max_length=50,null=True,blank=True)
    size = models.CharField(max_length=50,null=False,blank=False)
    images = models.FileField(upload_to=file_path)
    slug = models.SlugField()
    description = models.CharField(max_length=500,null=False,blank=False)
    review = models.CharField(max_length=250)
    
    class Meta:
        db_table = 'shoes'
        managed = True
        
    def __str__(self):
        return self.model+"||"+self.shoe_id
    
    # def get_absolute_url(self):
    #     return reverse("products:product", kwargs={"slug": self.slug})
    
    # def get_collection_url(self):
    #     return reverse("products:get_collections",kwargs={"slug":self.slug})
    
        
    

class Shoes_image(models.Model):
    
    product=models.ForeignKey(Shoe,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='static/images/shoes/shoes_DB/', height_field=None, width_field=None, max_length=None)
    
    class Meta:
        db_table = 'shoes_images'
        managed = True
