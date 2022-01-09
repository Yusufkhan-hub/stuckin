from django.shortcuts import render
from .models import Shoe,Shoes_image
# Create your views here.
from django.views.generic import ListView

# class product(ListView):
#     model = Shoe
#     template_name = "product.html"
#     slug_field='slug'


# class get_collection(ListView):
#     model = Shoe
#     template_name  = "base.html"
#     slug_field = 'slug'
    
# class collection(ListView):
#     model = Shoe
#     template_name = "shop.html"
#     slug_field = 'slug'
def collection(request):

    obj_all=Shoe.objects.all()
    shoes_images=Shoes_image.objects.all()
    context = {
        'obj_all':obj_all,
        'shoes_images':shoes_images
    }
    
    return render(request,'shop.html',context)
    
def product(request,shoe_id):        
    obj=Shoe.objects.filter(shoe_id=shoe_id)
    shoe_image = Shoes_image.objects.filter(product=shoe_id)
    # shoes_images=Shoes_image
    context = {
        'obj':obj,
        'shoe_images':shoe_image
    }        
    return render(request,'product.html',context)

    
# def product_page(request):
#     return render(request,'product.html')