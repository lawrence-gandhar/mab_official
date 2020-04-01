from django.forms import *
from app.models import *
from app.other_constants import *

class UploadContactsForm(ModelForm):
    class Meta:
        model = contacts_model.ContactsFileUpload
        fields = ('csv_file',)

        widgets = {
            'csv_file' : FileInput(attrs = {'class':'form-control input-sm', 'accept': ".csv", 'required':True,'style':'padding:1px'}),
        }

class ContactsForm(ModelForm):
    class Meta:

        model = contacts_model.Contacts
        fields = (
                    'customer_type', 'is_imported_user', 'imported_user', 'contact_name', 
                    'display_name', 'organization_name', 'organization_type', 'salutation',
                    'app_id', 'website', 'email', 'phone', 'facebook', 'twitter', 
                    'is_sub_customer', 'is_msme_reg', 'attachements', 'notes',
                )

        widgets = {
            'attachements' : FileInput(attrs = {'class':'form-control input-sm',}),
            'customer_type': Select(attrs={'class':'form-control input-sm',}, choices = user_constants.CUSTOMER_TYPE),
            'is_sub_customer': Select(attrs={'class':'form-control input-sm',}, choices = user_constants.IS_SUB_CUSTOMER),
            'is_msme_reg': Select(attrs={'class':'form-control input-sm',}, choices = user_constants.IS_TRUE),
            'is_imported_user': CheckboxInput(attrs={'class':'form-check-input','value':'1', 'style':'margin:5px; height:15px; width:15px;',}),
            'imported_user': TextInput(attrs={'class':'form-control input-sm', 'type':'hidden',}),
            'email': TextInput(attrs={'class':'form-control input-sm', 'placeholder':'abc@gmail.com', 'onkeyup':'valid_Email($(this))', 'onfocusout':'valid_Email($(this))' }),
            'phone': TextInput(attrs={'class':'form-control input-sm', 'type':'number','placeholder':'10 digit phone number','onkeyup':'valid_Phone($(this))', 'onfocusout':'valid_Phone($(this))'}),
            'website': TextInput(attrs={'class':'form-control input-sm', 'onkeyup':'valid_URL($(this))', 'onfocusout':'valid_URL($(this))'}),
            'salutation' : Select(attrs={'class':'form-control input-sm',}, choices = user_constants.SALUTATIONS),
            'contact_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200',}),
            'display_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200',}),
            'facebook' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200','onkeyup':'valid_URL($(this))', 'onfocusout':'valid_URL($(this))'}),
            'twitter' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200', 'onkeyup':'valid_URL($(this))', 'onfocusout':'valid_URL($(this))'}),
            'organization_type' : Select(attrs={'class':'form-control input-sm',}, choices = user_constants.ORGANIZATION_TYPE, ),
            'organization_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200', 'require':True,}),
            'notes': Textarea(attrs = {'class':'form-control',},)
        }

#
# ADDRESS FORM
#
class AddressForm(ModelForm):

    class Meta:
        model = users_model.User_Address_Details
        
        fields = ('contact_person', 'flat_no', 'street', 'city', 'state', 'country', 'pincode', 'is_billing_address_diff', 'is_shipping_address')
        
        widgets = {
            'contact_person' : TextInput(attrs={'class':'form-control input-sm','style':'width:40%;'}),
            'flat_no' : TextInput(attrs={'class':'form-control input-sm','style':'width:40%;'}),
            'street' : TextInput(attrs={'class':'form-control input-sm','style':'width:40%;'}),
            'city' : TextInput(attrs={'class':'form-control input-sm','style':'width:40%;'}),
            'state' : Select(attrs={'class':'form-control input-sm','style':'width:40%;'}, choices = country_list.STATE_LIST_CHOICES),
            'country' : Select(attrs={'class':'form-control input-sm','style':'width:40%;'}, choices = country_list.COUNTRIES_LIST_CHOICES),
            'pincode' : TextInput(attrs={'class':'form-control input-sm','style':'width:40%;'}),
            'is_billing_address_diff' : Select(attrs={'class':'form-control input-sm','style':'width:40%;','hidden':'true'}),
            'is_shipping_address' : Select(attrs={'class':'form-control input-sm','style':'width:40%;','hidden':'true'}),
        }

#
# ADDRESS FORM
#
class EditAddressForm(ModelForm):

    class Meta:
        model = users_model.User_Address_Details
        
        fields = ('contact_person', 'flat_no', 'street', 'city', 'state', 'country', 'pincode', 'is_billing_address', 'is_shipping_address')
        
        widgets = {
            'contact_person' : TextInput(attrs={'class':'form-control input-sm','style':'width:50%;'}),
            'flat_no' : TextInput(attrs={'class':'form-control input-sm','style':'width:50%;'}),
            'street' : TextInput(attrs={'class':'form-control input-sm','style':'width:50%;'}),
            'city' : TextInput(attrs={'class':'form-control input-sm','style':'width:50%;'}),
            'state' : Select(attrs={'class':'form-control input-sm','style':'width:50%;'}, choices = country_list.STATE_LIST_CHOICES),
            'country' : Select(attrs={'class':'form-control input-sm','style':'width:50%;'}, choices = country_list.COUNTRIES_LIST_CHOICES),
            'pincode' : TextInput(attrs={'class':'form-control input-sm','style':'width:50%;'}),
            'is_billing_address' : CheckboxInput(attrs={'class':'is_billing_address form-control input-sm','style':'width:50%;', 'required':'true'}),
            'is_shipping_address' : CheckboxInput(attrs={'class':'is_shipping_address form-control input-sm','style':'width:50%;', 'required':'false'}),
        }

#
# ACCOUNTS FORM
#
class AccountDetailsForm(ModelForm):
    class Meta:
        model = users_model.User_Account_Details
        fields = ('account_number', 'account_holder_name', 'ifsc_code', 'bank_name', 'bank_branch_name')

        widgets = {
            'account_number' : NumberInput(attrs={'class':'form-control input-sm', 'pattern':'[0-9]'}),
            'account_holder_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'ifsc_code' : TextInput(attrs={'class':'form-control input-sm', 'onkeyup':'valid_IFSC($(this))', 'onfocusout':'valid_IFSC($(this))'}),
            'bank_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'bank_branch_name' : TextInput(attrs={'class':'form-control input-sm',}),
        }


class ContactsExtraForm(ModelForm):
    class Meta:

        model = contacts_model.Contacts
        fields = ('website', 'facebook', 'twitter', 'attachements', 'notes',)

        widgets = {
            'attachements' : FileInput(attrs = {'class':'form-control input-sm','style':'padding:1px'}),
            'website': TextInput(attrs={'class':'form-control input-sm','placeholder':'http://google.com/', 'onkeyup':'valid_URL($(this))', 'onfocusout':'valid_URL($(this))'}),
            'facebook' : TextInput(attrs={'class':'form-control input-sm','placeholder':'http://facebook.com/', 'max_length':'200', }),
            'twitter' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200','placeholder':'http://twitter.com/', }),
            'notes': Textarea(attrs = {'class':'form-control',})
        }         

""""
class ContactsEmailForm(ModelForm):
    class Meta:
        EMAIL_CHOICES = ((True, 'Yes'),(False, 'No'))
        
        model = Contacts_Email
        fields = ('email', 'is_official', 'is_personal')

        widgets = {
            'email' : EmailInput(attrs={'class':'form-control input-sm',}),
            'is_official' : Select(attrs={'class':'form-control input-sm',}, choices = EMAIL_CHOICES, ),
            'is_personal' : Select(attrs={'class':'form-control input-sm',}, choices = EMAIL_CHOICES, ),
        }

class AccountDetailsForm(ModelForm):
    class Meta:
        model = Contact_Account_Details
        fields = ('account_number', 'account_holder_name', 'ifsc_code', 'bank_name', 'bank_branch_name')

        widgets = {
            'account_number' : TextInput(attrs={'class':'form-control input-sm',}),
            'account_holder_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'ifsc_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'bank_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'bank_branch_name' : TextInput(attrs={'class':'form-control input-sm',}),
        }

"""