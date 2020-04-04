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

    x = a[-4:-1]
    
    if(len(a) == 31):
        products = ProductsModel.objects.prefetch_related('productphotos_set').filter(user = request.user)
    else:
        search = a[37:(len(a))-2]
        products = ProductsModel.objects.filter(Q(user = request.user) & Q(sku__icontains = search) | Q(product_name__icontains = search))

    if(x == "on'" ):

        ProductType = request.GET.get('ProductType','off')
        Status = request.GET.get('status', 'off')
        
        Goods = request.GET.get('Goods', 'off')
        Services = request.GET.get('Services', 'off')
        Bundle = request.GET.get("Bundle", 'off')

        Is_Yes = request.GET.get('Yes', 'off')
        Is_No = request.GET.get('No', 'off')

        #Product type = on
        if(ProductType =="on" and Status == "off"):
            if(Goods =="on" and Services =="off" and Bundle =="off"):
                products = ProductsModel.objects.filter(user = request.user).filter(product_type = 0)
            elif(Goods =="off" and Services =="on" and Bundle == "off"):
                products = ProductsModel.objects.filter(user = request.user).filter(product_type = 1)
            elif(Goods =="off" and Services =="off" and Bundle =="on"):
                products = ProductsModel.objects.filter(user = request.user).filter(product_type = 2)
            elif(Goods =="on" and Services =="on" and Bundle =="off"):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = 0) | Q(product_type = 1))
            elif(Goods =="on" and Bundle =="on" and Services =="off"):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = 0) | Q(customer_type = 2))
            elif(Goods =="off" and Bundle =="on" and Services =="on"):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = 1) | Q(customer_type = 2))
            elif(Goods =="on" and Services =="on" and Bundle =="on"):
                products = ProductsModel.objects.filter(user = request.user)
            elif(Goods =="off" and Services =="off" and Bundle =="off"):
                products = ProductsModel.objects.filter(user = request.user)

        #Status Type = on
        if(ProductType =="off" and Status == "on"):
            if(Is_Yes == 'on' and Is_No == 'off'):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True))
            elif(Is_Yes == 'off' and Is_No == 'on'):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = False))
            elif(Is_Yes == 'on' and Is_No == 'on'):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False)) 
            elif(Is_Yes == 'off' and Is_No == 'off'):
                products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False)) 
        
        #Status Type = on & product type = on
        if(ProductType =="on" and Status == "on"):
            # goods=on
            if(Goods == "on" and Services == "off" and Bundle == "off"):
                a = ProductsModel.objects.filter(user = request.user).filter(product_type = 0)
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))

            elif(Goods == "off" and Services == "on" and Bundle == "off"):
                #  Services =="on"
                a = ProductsModel.objects.filter(user = request.user).filter(product_type = 1)
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))

            elif(Goods == "off" and Services == "off" and Bundle == "on"):
                # Bundle =="on"
                a = ProductsModel.objects.filter(user = request.user).filter(product_type = 2)
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))

            if(Goods == "on" and Services == "on" and Bundle == "off"):
                # Goods =="on" and Services =="on"
                a = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = 0) | Q(product_type = 1))
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))

            elif(Goods  =="on" and Services =="off" and Bundle =="on"):
                # Goods == "on" and Bundle =="on"
                a = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = 0) | Q(product_type = 2))
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                    
            elif(Goods  == "off" and Services == "on" and Bundle == "on"):
                # Services == "on" and Bundle =="on"
                a = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = 1) | Q(product_type = 2))
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))

            elif(Goods == "on" and Services == "on" and Bundle == "on"):
                # Goods =="on" and Services =="on" and Bundle =="on"
                a = ProductsModel.objects.filter(user = request.user)
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                
            elif(Goods =="off" and Services =="off" and Bundle =="off"):
                # Goods =="off" and Services == "off" and Bundle == "off"
                a = ProductsModel.objects.filter(user = request.user)
                if(Is_Yes == 'on' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True))
                elif(Is_Yes == 'off' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = False))
                elif(Is_Yes == 'on' and Is_No == 'on'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = a.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))
                elif(Is_Yes == 'off' and Is_No == 'off'):
                    products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True) | Q(is_active = False))

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
        

        product_names = request.POST.getlist("prod_name[]")
        qty = request.POST.getlist("qty[]")

        for i in range(len(product_names)):
            try:
                product = ProductsModel.objects.get(pk = int(product_names[i]))

                obj = BundleProducts(
                    product_bundle = ins,
                    product = product,
                    quantity = int(qty[i])
                )

                obj.save()
            except:
                pass

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
# BUNDLE - Commented by Lawrence
#===================================================================================================
#
""""
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

"""

def bundle(request):
    html = ['<option value="">------</option>']
    
    if request.GET:
        
        prod_type = request.GET["prod_type"]

        if prod_type != '':
            products = ProductsModel.objects.filter(user = request.user, product_type = prod_type).values("id","product_name")
            
            print(products)
            
            for product in products:
                html.append('<option value="{}">{}</option>'.format(product["id"], product["product_name"]))

    return HttpResponse(''.join(html))
