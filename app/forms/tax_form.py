from django.forms import *
from django.contrib.auth.models import User
from app.models.contacts_model import *
from app.models.users_model import *

class TaxForm(ModelForm):
    class Meta:
        model = User_Tax_Details
        fields = ('pan', 'gstin', 'gst_reg_type')

        widgets = {
            'pan' : TextInput(attrs = {'class':'form-control input-sm','placeholder':'Eg. ABCDE1234D','onkeyup':'valid_PAN($(this))', 'onfocusout':'valid_PAN($(this))'}), 
            'gstin' : TextInput(attrs = {'class':'form-control input-sm','placeholder':'Eg. 36ARVPS3698F1ZF', 'onkeyup':'valid_GST($(this))', 'onfocusout':'valid_GST($(this))'}), 
            'gst_reg_type' : Select(attrs = {'class':'form-control input-sm','id':'gst_reg','onchange':'hide_gst($(this))',}, choices = user_constants.GST_REG_TYPE), 
        }


class OtherDetailsForm(ModelForm):
    class Meta:
        model = User_Tax_Details
        fields = (
            'preferred_currency', 'opening_balance', 'preferred_payment_method', 
            'preferred_delivery', 'invoice_terms', 'bills_terms',
        )

        widgets = {
            'preferred_currency' : Select(attrs = {'class':'form-control input-sm','style':'width:50%;',}, choices = currency_list.CURRENCY_CHOICES), 
            'opening_balance' : TextInput(attrs = {'class':'form-control input-sm','style':'width:50%;','onkeypress':'return restrictAlphabets(event)',}),
            'preferred_payment_method' : Select(attrs = {'class':'form-control input-sm','style':'width:50%;',}, choices = payment_constants.PREFERRED_PAYMENT_TYPE), 
            'preferred_delivery' : Select(attrs = {'class':'form-control input-sm','style':'width:50%;',}, choices = payment_constants.PREFERRED_DELIVERY), 
            'invoice_terms' : Select(attrs = {'class':'form-control input-sm','style':'width:50%;',}, choices = payment_constants.PAYMENT_DAYS), 
            'bills_terms' : Select(attrs = {'class':'form-control input-sm','style':'width:50%;',}, choices = payment_constants.PAYMENT_DAYS), 
        }