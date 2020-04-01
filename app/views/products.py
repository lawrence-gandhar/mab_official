from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.db.models import *
from app.models import *
from app.forms.items_form import * 

import json


#========================================================================================
#   VIEW/LIST PRODUCTS
#========================================================================================
#
def view_products(request, *args, **kwargs):
    # Template 
    template_name = 'app/app_files/products/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/product.js',]
    data["active_link"] = 'Products'
    data["breadcrumb_title"] = 'PRODUCTS'

    data["included_template"] = 'app/app_files/products/view_products.html'

    #*****************************************************************************
    # PRODUCT LISTING
    #*****************************************************************************
    a = str(request)
    
    if(len(a) == 31):
        products = ProductsModel.objects.prefetch_related('productphotos_set').filter(user = request.user)
    else:
        search = a[37:(len(a))-2]
        products = ProductsModel.objects.filter(Q(user = request.user) & Q(sku__icontains = search) | Q(product_name__icontains = search))


    data["products"] = products

    return render(request, template_name, data)    

#========================================================================================
# ADD PRODUCT
#========================================================================================
# 
class AddProducts(View):

    # Template 
    template_name = 'app/app_files/products/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/product.js',]
    data["active_link"] = 'Products'

    data["included_template"] = 'app/app_files/products/add_products_form.html'

    data["add_product_images_form"] = ProductPhotosForm()
    #
    #
    #
    def get(self, request, *args, **kwargs):
        self.data["add_product_form"] = ProductForm(request.user)
        return render(request, self.template_name, self.data)

    def post(self, request, *args, **kwargs):                         
        
        add_product = ProductForm(request.user, request.POST or None)
        add_images = ProductPhotosForm(request.FILES or None)

        ins = None

        if add_product.is_valid():
            ins = add_product.save()            
            ins.user = request.user
            ins.save()
        
        if add_images.is_valid() and ins is not None:
            for img in request.FILES.getlist('product_image'):
                img_save = ProductPhotos(
                    product_image = img,
                    product = ins
                )

                img_save.save()

        return redirect('/products/', permanent = False)

#=========================================================================================
# PRODUCT DELETE
#=========================================================================================
#
def delete_product(request, ins = None):
    if ins is not None:
        try:
            product = ProductsModel.objects.get(pk = int(ins))
        except:
            return redirect('/unauthorized/', permanent=False)

        product.delete()
        return redirect('/products/', permanent=False)
    return redirect('/unauthorized/', permanent=False)


#===================================================================================================
# STATUS CHANGE
#===================================================================================================
#
def status_change(request, slug = None, ins = None):
    
    if slug is not None and ins is not None:
        try:
            product = ProductsModel.objects.get(pk = int(ins))        
        except:
           return redirect('/unauthorized/', permanent=False)

        if slug == 'deactivate':
            product.is_active = False
        elif slug == 'activate':
            product.is_active = True
        else:
            return redirect('/unauthorized/', permanent=False)

        product.save()
        return redirect('/products/', permanent=False)

    return redirect('/unauthorized/', permanent=False)


#===================================================================================================
# STATUS CHANGE
#===================================================================================================
#
class EditProducts(View):

    # Template 
    template_name = 'app/app_files/products/index.html'

    # Initialize 
    data = defaultdict()
    data["view"] = ""

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/product.js',]
    data["active_link"] = 'Products'

    data["included_template"] = 'app/app_files/products/add_products_form.html'

    data["add_product_images_form"] = ProductPhotosForm()
    
    #
    #
    #
    def get(self, request, *args, **kwargs):

        try:
            product = ProductsModel.objects.get(pk = int(kwargs["ins"]))
        except:
            return redirect('/unauthorized/', permanent=False)

        self.data["add_product_form"] = ProductForm(request.user, instance = product)
        return render(request, self.template_name, self.data)

    #
    #
    #
    def post(self, request, *args, **kwargs):
        try:
            product = ProductsModel.objects.get(pk = int(kwargs["ins"]))
        except:
            return redirect('/unauthorized/', permanent=False)

        add_product = ProductForm(request.user, request.POST or None, instance = product)
        add_images = ProductPhotosForm(request.FILES or None)

        ins = None

        if add_product.is_valid():
            ins = add_product.save()
            ins.user = request.user
            ins.save()
        
        if add_images.is_valid() and ins is not None:
            for img in request.FILES.getlist('product_image'):
                img_save = ProductPhotos(
                    product_image = img,
                    product = ins
                )

                img_save.save()
        
        return redirect('/products/', permanent = False)

#
#
#
def ajax_add_product(request):

    if request.POST and request.is_ajax():                        
        
        add_product = ProductForm(request.user, request.POST or None)
        add_images = ProductPhotosForm(request.FILES or None)

        ins = None

        if add_product.is_valid():
            ins = add_product.save()            
            ins.user = request.user
            ins.save()
        
        if add_images.is_valid() and ins is not None:
            for img in request.FILES.getlist('product_image'):
                img_save = ProductPhotos(
                    product_image = img,
                    product = ins
                )

                img_save.save()
        return HttpResponse(1)
    return HttpResponse(0)



#===================================================================================================
# BUNDLE 
#===================================================================================================
#

def bundle(request, slug):

    if(slug == 'GOODS'):
        product_type = 0
    elif(slug == 'SERVICES'):
        product_type = 1
    name = []
    products = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = product_type))
    for i in range(0,len(products)):
        name.append(products[i].product_name)

    data = {'products' : name}
    return JsonResponse(data)