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
def add_creditnote(request, slug = None, ins = None):

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
    contacts = Contacts.objects.filter(user = request.user)
    data["contacts"] = contacts

    # list product name

    products = ProductsModel.objects.filter(user = request.user)
    data["products"] = products

    return render(request, template_name, data)


#=====================================================================================
#   ADD CREDITNOTE
#=====================================================================================
#

def data(request, slug):
    print("aaaaaaaaaaaaaaaa")
    print(request)
     # Initialize 
    data = defaultdict()
    name = slug
    address = User_Address_Details.objects.filter(contact = name)
    print(address)
    # products = ProductsModel.objects.filter(Q(user = request.user) & Q(product_type = product_type))
    # for i in range(0,len(products)):
    #     name.append(products[i].product_name)

    # data = {'products' : name}
    return JsonResponse(data)