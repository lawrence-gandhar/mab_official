from django.forms import * 
from app.models.items_model import *
from app.other_constants import *

#===================================================================================
# PRODUCT FORM
#===================================================================================
#

class ProductForm(ModelForm):
        
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['sales_account'].queryset = ProductAccounts.objects.filter(user = self.user, is_sales = True, is_active = True,)
        self.fields['purchase_account'].queryset = ProductAccounts.objects.filter(user = self.user, is_sales = False, is_active = True,)
        
    class Meta:
        model = ProductsModel

        fields = (
            'product_type', 'sku', 'product_name', 'product_description', 'product_dimension', 
            'cost_price', 'marked_price', 'selling_price', 'discount', 'tax', 'gst', 'purchase_account',
            'hsn_code', 'abatement', 'unit', 'is_sales', 'is_purchase', 'sales_account', 
        )

        widgets = {
            'product_type' : Select(attrs = {'class':'form-control input-sm','style':'width:40%','onchange':'show_bundle($(this))'}, choices = items_constant.PRODUCT_TYPE),
            'sku' : TextInput(attrs = {'class':'form-control input-sm','style':'width:71%',}),
            'product_name' : TextInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'product_dimension' : TextInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'product_description' : Textarea(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'cost_price' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'marked_price' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'selling_price' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'discount' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'tax' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'gst' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'hsn_code' : TextInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'abatement' : NumberInput(attrs = {'class':'form-control input-sm','style':'width:40%',}),
            'unit' : Select(attrs = {'class':'form-control input-sm', 'style':'width:40%',}, choices = items_constant.UNITS),
            'is_sales' : CheckboxInput(attrs = {'class':'form-check-input input-sm', 'checked':'true', 'style':'width:40%',},),
            'is_purchase' : CheckboxInput(attrs = {'class':'form-check-input', 'checked':'true', 'style':'width:40%',},),
            'purchase_account' : Select(attrs = {'class':'form-control input-sm', 'style':'width:40%',},),
            'sales_account' : Select(attrs = {'class':'form-control input-sm', 'style':'width:40%',},),
        }

#==================================================================================
# PRODUCT IMAGE FORM
#==================================================================================
#

class ProductPhotosForm(ModelForm):

    class Meta:
        model = ProductPhotos

        fields= ('product_image',)

        widgets = {
            'product_image' : FileInput(attrs = {'class':'form-control input-sm', 'id':'files','name':'files[]','type':'file','multiple' : 'true', 'accept':'image/jpeg, image/png, image/gif,', 'style':'width:71%;padding:1px',})
        }

#==================================================================================
# INVENTORY FORM
#==================================================================================
#

class InventoryForm(ModelForm):

    class Meta:    
        model = Inventory

        fields = ('inventory_name', 'in_date',)

        widgets = {
            'inventory_name' : TextInput(attrs = {'class':'form-control input-sm'}),
            'in_date' : DateInput(attrs={'class':'form-control input-sm', 'type':'date', 'data-toggle':'datepicker'}),
        }

#==================================================================================
# INVENTORY PRODUCT FORM
#==================================================================================
#

class InventoryProductForm(ModelForm):

    def __init__(self, user, inv, *args, **kwargs):
        self.user = user
        super(InventoryProductForm, self).__init__(*args, **kwargs)
        
        # Exclude product, if already assigned to the inventory instance
        #
        products_in_inv = InventoryProduct.objects.filter(inventory_id = inv)
        self.fields['product'].queryset = ProductsModel.objects.filter(user = self.user).exclude(inventoryproduct__in = products_in_inv)
        
    class Meta:
        model = InventoryProduct

        fields = (
            'product', 'quantity', 'unit', 'threshold', 'stop_at_min_hold', 'notify_on_threshold',
            'notify_on_min_hold', 'min_hold_notify_trigger', 'threshold_notify_trigger'
        )
        
        widgets = {
            'product' : Select(attrs = {'class':'form-control input-sm', 'required':'true'}),
            'quantity' : NumberInput(attrs = {'class':'form-control input-sm'}),
            'unit' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.UNITS),
            'threshold' : NumberInput(attrs = {'class':'form-control input-sm'}),
            'stop_at_min_hold' : NumberInput(attrs = {'class':'form-control input-sm'}),
            'notify_on_threshold' : Select(attrs = {'class':'form-control input-sm'}, choices = user_constants.IS_TRUE),
            'notify_on_min_hold' : Select(attrs = {'class':'form-control input-sm'}, choices = user_constants.IS_TRUE),
            'threshold_notify_trigger' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.PRODUCT_STOCK_NOTIFICATION_TRIGGERS),
            'min_hold_notify_trigger' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.PRODUCT_STOCK_NOTIFICATION_TRIGGERS),
        }


#==================================================================================
# INVENTORY PRODUCT FORM
#==================================================================================
#

class InventoryProductEditForm(ModelForm):
    class Meta:
        model = InventoryProduct

        fields = (
            'quantity', 'unit', 'threshold', 'stop_at_min_hold', 'notify_on_threshold',
            'notify_on_min_hold', 'min_hold_notify_trigger', 'threshold_notify_trigger'
        )
        
        widgets = {
            'quantity' : NumberInput(attrs = {'class':'form-control input-sm'}),
            'unit' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.UNITS),
            'threshold' : NumberInput(attrs = {'class':'form-control input-sm'}),
            'stop_at_min_hold' : NumberInput(attrs = {'class':'form-control input-sm'}),
            'notify_on_threshold' : Select(attrs = {'class':'form-control input-sm'}, choices = user_constants.IS_TRUE),
            'notify_on_min_hold' : Select(attrs = {'class':'form-control input-sm'}, choices = user_constants.IS_TRUE),
            'threshold_notify_trigger' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.PRODUCT_STOCK_NOTIFICATION_TRIGGERS),
            'min_hold_notify_trigger' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.PRODUCT_STOCK_NOTIFICATION_TRIGGERS),
        }
