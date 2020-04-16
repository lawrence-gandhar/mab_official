from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts
from app.models.users_model import *
from app.models.items_model import *

from django.db.models import Q

import json, os, csv


#=====================================================================================
#   CREDIT NOTE VIEW
#=====================================================================================
#

class CreditView(View):

    # Template 
    template_name = 'app/app_files/creditnote/base.html'
    
    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["contacts"] = {}
    data["active_link"] = 'Credit Note'
    data["breadcrumb_title"] = 'Credit Note'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["included_template"] = 'app/app_files/creditnote/view_creditnote.html'
    
    #
    #
    def get(self, request):        

        # view_type = request.GET.get('view',False)

        # contacts = Contacts.objects.filter(user = request.user)
        # self.data["contacts"] = contacts

        # if view_type:
        #     self.data["view"] = "grid"
        # else:
        #     self.data["view"] = ""

        return render(request, self.template_name, self.data)

#=====================================================================================
#   ADD CREDITNOTE
#=====================================================================================
#
def add_creditnote(request, slug ):

    # Initialize 
    data = defaultdict()

    # Template 
    template_name = 'app/app_files/creditnote/base.html'
    data["included_template"] = 'app/app_files/creditnote/add_creditnote.html'
    
    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/creditnote.js']

    # Set link as active in menubar
    data["active_link"] = 'Credit Note'
    data["breadcrumb_title"] = 'Credit Note'

    # list contact name
    contacts = Contacts.objects.filter(Q(user = request.user) & Q(is_active = True))
    data["contacts"] = contacts
    Unit = ['Kilogram','Grams','Ounce','Pound','Tons','Metric Tons','Carat','Furlong','Inches','Foot','Yard','Mile','Meter','Millimetres',
            'Square Feet','Square Metre','Centimetre','Bucket','Bag','Bowl','Box','Card','Case','Carton','Dozen','Each','Gallon','Gross',
            'Kit','Set','Sheet','Tube','Pack','Teaspoon','Tablespoon','Cup','Pint','Quart','Milliliter','Liter']

    state = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujrat','Haryaba','Himachal Pradesh','Jammu And Kashmir',
            'Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Odisha','Punjab','Rajesthan',
            'Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
    data["unit"] = Unit
    data["state"] = state
    # list product name
    if( int(slug) == 1):
        products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True))
        name = []
        ids =[]
        count = len(products)
        for i in range(0,count):
            name.append(products[i].product_name)
            ids.append(products[i].id)
        data = {'products': name, 'ids': ids , 'unit':Unit ,} 
        return JsonResponse(data)
    elif(int(slug) == 0):
        products = ProductsModel.objects.filter(Q(user = request.user) & Q(is_active = True))
        data["products"] = products
        return render(request, template_name, data)


#=====================================================================================
#   FETCH CONTACT
#=====================================================================================
#

def fetch_contact(request, slug):
     # Initialize 
    data = defaultdict()
    
    contacts = Contacts.objects.get(Q(user = request.user) & Q(pk = int(slug)))
    data['contacts'] =  contacts.email 
    data['address'] = []
    address = User_Address_Details.objects.filter(contact = slug).values('contact_person','flat_no', 'street', 'city', 'state', 'country', 'pincode')
    for i in range(0,len(address)):
        add="Contact :- "
        for j in address[i].values():
            if( j is not None):
                add+=str(j)+', '
        data['address'].append(add[0:(len(add))-2])
    return JsonResponse(data)

#=====================================================================================
#   FETCH PRODUCT_type/Units/Price/Product Description
#=====================================================================================
#
def fetch_product(request, slug):
    
    # Initialize 
    data = defaultdict()
    Unit = ['Kilogram','Grams','Ounce','Pound','Tons','Metric Tons','Carat','Furlong','Inches','Foot','Yard','Mile','Meter','Millimetres',
            'Square Feet','Square Metre','Centimetre','Bucket','Bag','Bowl','Box','Card','Case','Carton','Dozen','Each','Gallon','Gross',
            'Kit','Set','Sheet','Tube','Pack','Teaspoon','Tablespoon','Cup','Pint','Quart','Milliliter','Liter']
    products = ProductsModel.objects.get(pk = int(slug))
    data['product'] = products.product_type
    data['unit'] = Unit[products.unit]
    data['price'] =  products.selling_price
    data['desc'] = products.product_description
    return JsonResponse(data)