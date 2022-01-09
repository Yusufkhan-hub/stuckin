from django.shortcuts import render
from products.models import Shoe
from django.views.generic import ListView,DetailView
# Create your views here.

def home(request):
    return render(request,'home.html')

class collection(ListView):
    model = Shoe
    template_name = 'shop.html'

# def collection(request):
    
#     obj_all=Shoe.objects.all()
#     # shoes_images=Shoes_image.objects.all()
#     context = {
#         'obj_all':obj_all,
#         # 'shoes_images':shoes_images
#     }
    
#     return render(request,'shop.html',context)
    