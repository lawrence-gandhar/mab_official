from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.contrib import messages

from app.models.contacts_model import Contacts, Contacts_Email, Contact_Addresses, Contact_Account_Details, ContactsFileUpload
from app.models.users_model import *
from app.forms.contact_forms import *
from app.forms.tax_form import *

from django.conf import *

from django.db import *

import json, os, csv

#=====================================================================================
#   CONTACTS VIEW
#=====================================================================================
#
class ContactsView(View):

    # Template 
    template_name = 'app/app_files/contacts/base.html'
    
    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["contacts"] = {}
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["included_template"] = 'app/app_files/contacts/view_contacts.html'
    
    #
    #
    def get(self, request):        

        view_type = request.GET.get('view',False)

        contacts = Contacts.objects.filter(user = request.user)
        self.data["contacts"] = contacts

        if view_type:
            self.data["view"] = "grid"
        else:
            self.data["view"] = ""

        return render(request, self.template_name, self.data)


#=====================================================================================
#   ADD CONTACTS
#=====================================================================================
#
def add_contacts(request, slug = None, ins = None):

    # Initialize 
    data = defaultdict()

    # Template 
    template_name = 'app/app_files/contacts/base.html'
    data["included_template"] = 'app/app_files/contacts/add_contacts_step1.html'
    
    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = ['custom_files/js/contacts.js']

    # Set link as active in menubar
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    data["slug"] = slug
    data["breadcrumbs"] = ''
    data["breadcrumbs_index"] = 0
    
    data["instance_title"] = None
    data["contact_form_instance"] = ins
    data["query_string"] = request.GET.get('section', None)

    # Initialize Forms
    data["contact_form"] = ContactsForm()
    data["tax_form"] = TaxForm()
    data["contact_email_form"] = ContactsEmailForm()
    data["contact_address_form"] = ContactsAddressForm()
    data["contact_account_details_form"] = ContactAccountDetailsForm()

    #***************************************************************
    # Breadcrumbs List & Links
    #***************************************************************

    qStr = ''
    if data["query_string"] is not None and data["query_string"] == 'all':
        qStr = '?section='+data["query_string"]

    breadcrumbs_list = [
            '<li class="nav-item" style="float:left;padding:0px 10px;"><a href="/contacts/add/step1/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="material-icons">account_circle</i> <span style="position:relative; top: 2px;">Basic Details</span></a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step2/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="material-icons">account_balance</i> <span style="position:relative; top: 2px;">Tax Details</span></a></li>',            
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step3/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="material-icons">house</i> <span style="position:relative; top: 2px;">Address Details</span></a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step4/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="material-icons">credit_card</i> <span style="position:relative; top: 2px;">Account Details</span></a></li>',
            '<li class="nav-item" style="float:left;padding:0px 10px; margin-left:10px;"><a href="/contacts/add/step5/'+ str(data["contact_form_instance"]) +qStr+'" style="color:#FFFFFF; text-decoration:none;"><i class="material-icons">mail</i> <span style="position:relative; top: 2px;">Email Details</span></a></li>',
        ]

    if ins is not None:
        try: 
            contact = Contacts.objects.get(pk = data["contact_form_instance"], user = request.user)
            data["instance_title"] = contact.contact_name
        except:
            return redirect('/unauthorized/', permanent = True)

    #***************************************************************
    # Check SLUG - for creation of Forms 
    #***************************************************************

    if data["slug"] is not None and data["contact_form_instance"] is not None:
        
        data["breadcrumbs_index"] = int(data["slug"].replace('step',''))

        if data["contact_form_instance"] is None:
            data["included_template"] = 'app/app_files/contacts/add_contacts_'+data["slug"]+'.html'
        else:
            template_name = 'app/app_files/contacts/edit_contacts.html'
            try:
                if data["breadcrumbs_index"] == 1:
                    data["contact_form"] = ContactsForm(instance = contact)
                    counter = 1

                if data["breadcrumbs_index"] == 2:
                    try:
                        tax_record = User_Tax_Details.objects.get(contact = contact, is_user = False)
                        counter = 1
                        data["tax_form"] = TaxForm(instance = tax_record)
                    except:
                        counter = 0
                        data["tax_form"] = TaxForm()
                    
                    
                if data["breadcrumbs_index"] == 3:
                    data["contact_addresses"] = Contact_Addresses.objects.filter(contact = data["contact_form_instance"])
                    counter = data["contact_addresses"].count()
                    
                if data["breadcrumbs_index"] == 4:                    
                    data["contact_account_details"] = Contact_Account_Details.objects.filter(contact = data["contact_form_instance"])
                    counter = data["contact_account_details"].count()

                if data["breadcrumbs_index"] == 5:
                    data["contact_emails"] = Contacts_Email.objects.filter(contact = data["contact_form_instance"])
                    counter = data["contact_emails"].count()

                if counter == 0 :
                    data["included_template"] = 'app/app_files/contacts/add_contacts_'+data["slug"]+'.html'
                else:
                    data["included_template"] = 'app/app_files/contacts/edit_contacts_'+data["slug"]+'.html'
                
            except:
                data["included_template"] = 'app/app_files/contacts/add_contacts_'+data["slug"]+'.html'

        breadcrumbs = []
        for i in range(data["breadcrumbs_index"]):
            breadcrumbs.append(breadcrumbs_list[i])

        data["breadcrumbs"] = ''.join(breadcrumbs)

    #***************************************************************
    # Check QueryString - for creation of breadcrumbs 
    #***************************************************************

    if data["query_string"] is not None:
        if data["query_string"] == '':
            return redirect('/unauthorized/', permanent = True)
        elif data["query_string"] == 'all':
            data["breadcrumbs"] = ''.join(breadcrumbs_list)
        else:
            return redirect('/unauthorized/', permanent = True)

    #***************************************************************
    # POST REQUEST
    #***************************************************************

    if request.POST:

        if data["slug"] is None:
            contact_form = ContactsForm(request.POST, request.FILES)
            if contact_form.is_valid():
                data["contact_form_instance"] = contact_form_ins = contact_form.save(commit = False)
                contact_form_ins.user = request.user

                if contact_form_ins.is_imported_user:
                    try:
                        profile = Profile.objects.get(app_id__iexact = contact_form_ins.app_id)
                        imp_user = User.objects.get(pk = profile.user_id)
                    except:
                        return redirect('/unauthorized/', permanent = False)
                    
                    contact_form_ins.imported_user = imp_user
                
                contact_form_ins.save()
                
                if contact_form_ins.email is not None:
                    email_ins = Contacts_Email.objects.create(contact = contact_form_ins)
                    email_ins.email = contact_form_ins.email
                    email_ins.is_official = True
                    email_ins.save()

                return redirect('/contacts/add/step2/{}'.format(data["contact_form_instance"].pk), permanent=False) 
        
        try:
            c = Contacts.objects.get(pk = data["contact_form_instance"], user = request.user)
        except Contacts.DoesNotExist:
            return redirect('/unauthorized/', permanent = False)

        if data["breadcrumbs_index"] == 2: 
            contacts_tax_form = TaxForm(request.POST or None)
            if contacts_tax_form.is_valid():
                obj = contacts_tax_form.save()
                obj.contact = c
                obj.save()
                return redirect('/contacts/add/step3/{}'.format(data["contact_form_instance"]), permanent=False) 

        if data["breadcrumbs_index"] == 3:            
            contact_address_form = ContactsAddressForm(request.POST or None)
            if contact_address_form.is_valid():
                contact_address = contact_address_form.save(commit = False)    
                contact_address.contact = c
                contact_address.save()                 
                return redirect('/contacts/add/step4/{}'.format(data["contact_form_instance"]), permanent=False) 
            
        if data["breadcrumbs_index"] == 4:            
            contact_account_details_form = ContactAccountDetailsForm(request.POST or None)
            if contact_account_details_form.is_valid():
                contact_account_details = contact_account_details_form.save(commit = False)    
                contact_account_details.contact = c
                contact_account_details.save()                
                return redirect('/contacts/add/step5/{}'.format(data["contact_form_instance"]), permanent=False) 

        if data["breadcrumbs_index"] == 5:          
            contact_email_form = ContactsEmailForm(request.POST or None)
            if contact_email_form.is_valid():
                contact_email = contact_email_form.save(commit = False)    
                contact_email.contact = c
                contact_email.save()
                return redirect('/contacts/add/step5/{}'.format(data["contact_form_instance"]), permanent=False) 
            

    return render(request, template_name, data)


#=====================================================================================
#   EDIT CONTACTS
#=====================================================================================
#
def edit_contact(request, slug = None, ins = None):
    if request.POST:
        if slug is not None and ins is not None:
            try:
                contact = Contacts.objects.get(pk = int(ins), user = request.user)
                contact_form = ContactsForm(request.POST, instance = contact)
                
                if contact_form.is_valid(): 
                    contact_form.save()    
            except:
                return redirect('/unauthorized/', permanent=False)
    return redirect('/contacts/add/step1/{}'.format(ins), permanent=False)

#=======================================================================================
#   FETCH EDIT CONTACT EXTRA FORMS
#=======================================================================================
#
def fetch_extra_edit_forms(request):
    if request.is_ajax():
        if request.POST:
            form_type = request.POST.get('form_type', None)
            obj_ins = request.POST.get('ins', None)

            form_html = OrderedDict()

            if form_type is not None and obj_ins is not None:
                
                #***************************************************************
                # Edit Email Form
                #***************************************************************

                if form_type == 'edit_contact_email':
                    labels = {
                        'email' : 'Email Address',
                        'is_official' : 'Is Official Email',
                        'is_personal' : 'Is Personal Email'
                    }
                    try:
                        obj = Contacts_Email.objects.get(pk = int(obj_ins))
                        form_data = ContactsEmailForm(instance = obj) 
                    except:
                        return HttpResponse('0')

                #***************************************************************
                # Edit Address Form
                #***************************************************************

                if form_type == 'edit_contact_address':
                    labels = {
                        'contact_name' : 'Contact Person',
                        'flat_no' : 'Flat/Door No',
                        'street' : 'Street/Lane',
                        'city' : 'City',
                        'state' : 'State',
                        'country' : 'Country',
                        'pincode' : 'Zip Code',
                        'is_billing_address' : 'Is Billing Address',
                        'is_shipping_address' : 'Is Shipping Address',
                    }
                    try:
                        obj = Contact_Addresses.objects.get(pk = int(obj_ins))
                        form_data = ContactsAddressForm(instance = obj)
                    except:
                        return HttpResponse('0')

                #***************************************************************
                # Edit Account Form
                #***************************************************************

                if form_type == 'edit_contact_account_details':
                    labels = {
                        'account_number':'Account Number',
                        'account_holder_name':'Account Holder',
                        'ifsc_code':'IFSC Code',
                        'bank_name':'Bank Name',
                        'bank_branch_name':'Branch Name',
                    }

                    try:
                        obj = Contact_Account_Details.objects.get(pk = int(obj_ins))
                        form_data = ContactAccountDetailsForm(instance = obj)
                    except:
                        return HttpResponse('0')


                #***************************************************************
                # Convert Form Fields to JSON
                #***************************************************************
                           
                form_html["id"] = {
                    'label':'id', 
                    'field':'<input type="hidden" value="'+obj_ins+'" name="id">', 
                    'label_style':'display:none'
                }
                for key in form_data.fields:
                    form_html[key] = {
                        'label': labels[key], 
                        'field':str(form_data[key]).replace("\n",""),
                        'label_style':''
                    }
                return HttpResponse(json.dumps(form_html))

            return HttpResponse('0')
        return HttpResponse('0')
    return HttpResponse('0')


#=======================================================================================
#   DELETE CONTACTS
#=======================================================================================
#
def delete_contacts(request, slug = None, ins = None, obj = None):

    if slug is not None and ins is not None and obj is not None:
        try: 
            contact = Contacts.objects.get(pk = ins, user = request.user)
        except:
            return redirect('/unauthorized/', permanent = True)

        slug = int(slug.replace('step',''))

        #***************************************************************
        # DELETE CONTACTS EMAIL
        #***************************************************************

        if slug == 2:
            try:
                CE = Contacts_Email.objects.get(pk = obj, contact = contact)
                Contacts_Email.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step2/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)

        #***************************************************************
        # DELETE CONTACTS ADDRESS
        #***************************************************************

        if slug == 3:
            try:
                CE = Contact_Addresses.objects.get(pk = obj, contact = contact)
                Contact_Addresses.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step3/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)
    
        #***************************************************************
        # DELETE CONTACTS ACCOUNT DETAILS
        #***************************************************************

        if slug == 4:
            try:
                CE = Contact_Account_Details.objects.get(pk = obj, contact = contact)
                Contact_Account_Details.objects.get(pk = obj).delete()
                return redirect('/contacts/add/step4/{}'.format(ins), permanent=True)
            except CE.DoesNotExists:
                return redirect('/unauthorized/', permanent = True)
        
    return redirect('/unauthorized/', permanent = True)

#================================================================================
# EDIT CONTACT FORMS 
#================================================================================

def edit_contact_forms(request):
    if request.POST:
        slug = request.POST.get('slug', None)
        obj_ins = request.POST.get('id', None)
        form_ins = request.POST.get('form_ins', None)

        if slug is not None and obj_ins is not None:

            redirect_url = False

            #***************************************************************
            # EDIT EMAIL
            #***************************************************************

            if slug == "step2":
                obj = Contacts_Email.objects.get(pk = int(obj_ins))
                email_form = ContactsEmailForm(request.POST, instance = obj)
                
                if email_form.is_valid():
                    email_form.save()
                    redirect_url = True
            
            #***************************************************************
            # EDIT ADDRESS DETAILS
            #***************************************************************

            if slug == "step3":
                obj = Contact_Addresses.objects.get(pk = int(obj_ins))
                address_form = ContactsAddressForm(request.POST, instance = obj)

                if address_form.is_valid():
                    address_form.save()
                    redirect_url = True

            #***************************************************************
            # EDIT ACCOUNT DETAILS
            #***************************************************************

            if slug == "step4":
                obj = Contact_Account_Details.objects.get(pk = int(obj_ins))
                accounts_form = ContactAccountDetailsForm(request.POST, instance = obj)

                if accounts_form.is_valid():
                    accounts_form.save()
                    redirect_url = True

            #***************************************************************
            # REDIRECTION ON SUCCESS OR FAILURE
            #***************************************************************

            if redirect_url:                
                return redirect('/contacts/add/{}/{}'.format(slug, form_ins), permanent=True)
            return redirect('/unauthorized/', permanent = True)
        return redirect('/unauthorized/', permanent = True)
    return redirect('/unauthorized/', permanent = True)


#================================================================================
# CHECK APPLICATION ID
# GET USER ID BASED ON THE CHECK
#================================================================================

def get_app_user_id(app_id):
    data = {'ret':0, 'id':None}
    try:
        pro = Profile.objects.get(app_id__iexact = app_id)
        data["ret"] = 1
        data["id"] = pro.user_id
    except:
        pass
    return data

#================================================================================
# CHECK APPLICATION ID
#================================================================================

def count_user_in_contact_list(user_id, imp_user_id):
    return Contacts.objects.filter(user = user_id, imported_user_id = int(imp_user_id)).count()

#================================================================================
# USER - CONTACT ALREADY PRESENT IN THE CONTACT LIST
#================================================================================

def check_app_id(request):
    data = {}
    if request.is_ajax():
        if request.POST: 
            data = get_app_user_id(request.POST["id"])
    return HttpResponse(json.dumps(data))


#================================================================================
# CHECK APPLICATION ID EXISTS IN THE CONTACT LIST
#================================================================================

def user_exists_in_list(request):
    if request.is_ajax():
        if request.POST:
            total = count_user_in_contact_list(request.user, request.POST["id"])
            return HttpResponse(total)    
        return HttpResponse(-1)
    return HttpResponse(-1)

#================================================================================
# CONTACTS FILE UPLOAD VIEW
#================================================================================

class ContactsFileUploadView(View):
    
    # Template 
    template_name = 'app/app_files/contacts/base.html'
    
    # Initialize 
    data = defaultdict()
    data["view"] = ""
    data["contacts"] = {}
    data["active_link"] = 'Contacts'
    data["breadcrumb_title"] = 'CONTACTS'

    # Custom CSS/JS Files For Inclusion into template
    data["css_files"] = []
    data["js_files"] = []

    data["included_template"] = 'app/app_files/contacts/upload_contacts.html'
    
    data["error_now"] = []
    data["row_count"] = 0

    # Documentation Import
    data["documentation_dict"] = documentation_dict.CSV_IMPORT_DICT

    #
    #
    def get(self, request):        
        self.data["error"] = ""
        self.data["upload_form"] = UploadContactsForm()
        return render(request, self.template_name, self.data)

    def post(self, request):
        self.data["upload_form"] = UploadContactsForm(request.POST, request.FILES)

        if self.data["upload_form"].is_valid():

            if str(request.FILES['csv_file']).lower().endswith('.csv'):

                self.data["upload_form"].save(commit = False)
                self.data["upload_form"].user = request.user
                obj = self.data["upload_form"].save()

                #***************************************************************
                #   Write data to database
                #***************************************************************

                file_path = settings.MEDIA_ROOT+"/"+str(obj.csv_file)
                err, self.data["row_count"] = csv_2_contacts(request.user,file_path)

                self.data["error"] = '<br>'.join(err)
            else:
                self.data["error"] = "Only CSV file is supported"
        return render(request, self.template_name, self.data)

#==============================================================================
# Function to insert contact import csv data into database
#==============================================================================
#
def csv_2_contacts(user, file_path):
    row_count = 0
    error_row = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        records = csv.DictReader(csvfile)

        fields = records.fieldnames

        contact_ins = None

        for row in records:

            #*************************************************************** 
            # Get and Set Missing/Existence of fields
            #***************************************************************
            salutation = row["salutation"] if "salutation" in fields else None
            customer_type = row["customer_type"] if "customer_type" in fields else None
            is_sub_customer = row["is_sub_customer"] if "is_sub_customer" in fields else 1
            contact_name = row["contact_name"] if "contact_name" in fields else None
            display_name = row["display_name"] if "display_name" in fields else None
            organization_type = row["organisation_type"] if "organisation_type" in fields else 1
            organization_name = row["organisation_name"] if "organisation_name" in fields else None
            
            if "is_msme_reg" in fields:
                is_msme_reg = True if row["is_msme_reg"] == 'TRUE' else False
            else:
                is_msme_reg = False

            email = row["email"] if "email" in fields else None
            phone = row["phone"] if "phone" in fields else None
            website = row["website"] if "website" in fields else None
            facebook = row["facebook"] if "facebook" in fields else None
            twitter = row["twitter"] if "twitter" in fields else None
            notes = row["notes"] if "notes" in fields else None

            contact_person = row["contact_person"] if "contact_person" in fields else None
            flat_no = row["flat_door_no"] if "flat_door_no" in fields else None
            street = row["street"] if "street" in fields else None
            city = row["city"] if "city" in fields else None
            pincode = row["pincode"] if "pincode" in fields else None
            state = row["state"] if "state" in fields else None
            country = row["country"] if "country" in fields else None

            account_number = row["account_number"] if "account_number" in fields else None 
            account_holder_name = row["account_holder_name"] if "account_holder_name" in fields else None 
            ifsc_code = row["ifsc_code"] if "ifsc_code" in fields else None 
            bank_name = row["bank_name"] if "bank_name" in fields else None 
            bank_branch_name = row["branch_name"] if "branch_name" in fields else None
            
            pan = row["pan"] if "pan" in fields else None
            gstin = row["gstin"] if "gstin" in fields else None
            gst_reg_type = row["gst_reg_type"] if "gst_reg_type" in fields else None
            business_reg_no = row["business_reg_no"] if "business_reg_no" in fields else None
            tax_reg_no = row["tax_reg_no"] if "tax_reg_no" in fields else None
            cst_reg_no = row["cst_reg_no"] if "cst_reg_no" in fields else None
            tds = row["tds"] if "tds" in fields else None
            preferred_currency = row["preferred_currency"] if "preferred_currency" in fields else None
            opening_balance = row["opening_balance"] if "opening_balance" in fields else None
            as_of = row["as_of"] if "as_of" in fields else None
            preferred_payment_method = row["preferred_payment_method"] if "preferred_payment_method" in fields else None
            preferred_delivery = row["preferred_delivery"] if "preferred_delivery" in fields else None
            invoice_terms = row["invoice_terms"] if "invoice_terms" in fields else None
            bills_terms = row["billing_terms"] if "billing_terms" in fields else None

            #***************************************************************
            # Phase 1
            #***************************************************************

            if row["is_parent_record"] == 'TRUE':
                
                #***************************************************************
                # Initiate Create
                #***************************************************************

                contact = Contacts(
                    salutation = salutation,
                    customer_type = customer_type,
                    is_sub_customer = is_sub_customer,
                    contact_name = contact_name,
                    display_name = display_name,
                    organization_type = organization_type,
                    organization_name = organization_name,
                    is_msme_reg = is_msme_reg,
                    email = email,
                    phone = phone,
                    website = website,
                    facebook = facebook,
                    twitter = twitter,
                    user = user,
                    notes = notes,
                )
                
                #***************************************************************
                #   If @ret is TRUE and user is not present in the  
                #   contact list then add user to contact list.
                #   If user is present then overwrite the data with the 
                #   csv record data.
                #***************************************************************  
                 
                if row["app_id"].strip() !="":
                    ret = get_app_user_id(row["app_id"])

                    if ret["ret"] == 1:                        
                        if count_user_in_contact_list(user, ret["id"]) == 0:
                            contact.save()

                            contact.imported_user_id = ret["id"]
                            contact.app_id = row["app_id"]

                            if row["use_app_user_details"] == 'TRUE': 
                                contact.is_imported_user = True
                                
                            contact.save()
                            contact_ins = contact
                        else:
                            #***************************************************************
                            # Initiate Update
                            #***************************************************************

                            contact_ins = contact = Contacts.objects.get(app_id__iexact = row["app_id"], user = user)
                            contact.salutation = salutation
                            contact.customer_type = customer_type
                            contact.is_sub_customer = is_sub_customer
                            contact.contact_name = contact_name
                            contact.display_name = display_name
                            contact.organization_type = organization_type
                            contact.organization_name = organization_name
                            contact.is_msme_reg = is_msme_reg
                            contact.email = email
                            contact.phone = phone
                            contact.website = website
                            contact.facebook = facebook
                            contact.twitter = twitter
                            contact.notes = notes
                            contact.save()
                    else:
                        error_row.append("Error On Row {}: In-Valid APP ID. Row Skipped".format(row_count))    
                        contact_ins = None
                else:
                    contact.save()
                    contact_ins = contact
                row_count += 1

            #***************************************************************
            # Phase 2
            #***************************************************************

            if contact_ins is not None:
                
                #***************************************************************
                # Address Details
                #***************************************************************

                if "is_contact_address" in fields and row["is_contact_address"] == "TRUE":
                
                    is_billing_address = False
                    is_shipping_address = False

                    if "is_billing_address" in fields and row["is_billing_address"] == "True":
                        is_billing_address = True

                    if "is_shipping_address" in fields and row["is_shipping_address"] == "True":
                        is_shipping_address = True

                    contact_address = Contact_Addresses(
                        contact_name = contact_person, 
                        flat_no = flat_no,
                        street = street,
                        city = city,
                        pincode = pincode,
                        state = state,
                        country = country,
                        is_billing_address = is_billing_address,
                        is_shipping_address = is_shipping_address,
                        contact = contact_ins,
                    )
                    contact_address.save()

                #***************************************************************
                # Account Details
                #***************************************************************

                if "is_contact_account_details" in fields and row["is_contact_account_details"] == "TRUE":
                    
                    contact_account_details = Contact_Account_Details(
                        contact = contact_ins,
                        account_number = account_number,
                        account_holder_name = account_holder_name,
                        ifsc_code = ifsc_code,
                        bank_name = bank_name,
                        bank_branch_name = bank_branch_name,
                    )
                    contact_account_details.save()

                #***************************************************************
                # Tax Details
                #***************************************************************
                if "is_contact_tax_details" in fields and row["is_contact_tax_details"] == "TRUE":
                    try:
                        tax_details = User_Tax_Details.objects.get(contact = contact_ins)

                        tax_details.pan = pan
                        tax_details.gstin = gstin
                        tax_details.gst_reg_type = gst_reg_type
                        tax_details.business_reg_no = business_reg_no
                        tax_details.tax_reg_no = tax_reg_no
                        tax_details.cst_reg_no = cst_reg_no
                        tax_details.preferred_currency = preferred_currency
                        tax_details.opening_balance = opening_balance
                        tax_details.as_of = as_of
                        tax_details.preferred_payment_method = preferred_payment_method
                        tax_details.preferred_delivery = preferred_delivery
                        tax_details.invoice_terms = invoice_terms
                        tax_details.bills_terms = bills_terms

                    except:
                        tax_details = User_Tax_Details(
                            is_user = False,
                            contact = contact_ins,
                            pan = pan,
                            gstin = gstin,
                            gst_reg_type = gst_reg_type,
                            business_reg_no = business_reg_no,
                            tax_reg_no = tax_reg_no,
                            cst_reg_no = cst_reg_no,
                            preferred_currency = preferred_currency,
                            opening_balance = opening_balance,
                            as_of = as_of,
                            preferred_payment_method = preferred_payment_method,
                            preferred_delivery = preferred_delivery,
                            invoice_terms = invoice_terms,
                            bills_terms = bills_terms,
                        )
                    
                    tax_details.save()

    return error_row, row_count

#===================================================================================================
# STATUS CHANGE
#===================================================================================================
#
def status_change(request, slug = None, ins = None):
    
    if slug is not None and ins is not None:
        try:
            contact = Contacts.objects.get(pk = int(ins))        
        except:
           return redirect('/unauthorized/', permanent=False)

        if slug == 'deactivate':
            contact.is_active = False
        elif slug == 'activate':
            contact.is_active = True
        else:
            return redirect('/unauthorized/', permanent=False)

        contact.save()
        return redirect('/contacts/', permanent=False)

    return redirect('/unauthorized/', permanent=False)


#===================================================================================================
# DELETE CHANGE
#===================================================================================================
#

def delete_contact(request, ins = None):
    if ins is not None:
        try:
            contact = Contacts.objects.get(pk = int(ins))
        except:
            return redirect('/unauthorized/', permanent=False)

        contact.delete()
        return redirect('/contacts/', permanent=False)
    return redirect('/unauthorized/', permanent=False)

        

