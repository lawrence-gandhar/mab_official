from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages


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
#   ADD CONTACTS
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
    data["js_files"] = ['custom_files/js/contacts.js']

    # Set link as active in menubar
    data["active_link"] = 'Credit Note'
    data["breadcrumb_title"] = 'Credit Note'

    # Initialize Forms
    
    # data["contact_form"] = ContactsForm()
    # data["social_form"] = ContactsExtraForm()
    # data["tax_form"] = TaxForm()
    # data["other_details_form"] = OtherDetailsForm()
    # data["contact_address_form_1"] = ContactsAddressForm(prefix = 'form1')
    # data["contact_address_form_2"] = ContactsAddressForm(prefix = 'form2')
    # data["contact_account_details_form"] = ContactAccountDetailsForm()

    #
    #
    #
     
    return render(request, template_name, data)

