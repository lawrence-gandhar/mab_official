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
        
    class Meta:
        model = ProductsModel

        fields = (
            'product_type', 'sku', 'product_name', 'product_description', 
            'cost_price','selling_price', 'discount', 'tax', 'gst', 'purchase_account',
            'hsn_code', 'abatement', 'unit', 'sales_account', 
        )

        widgets = {
            'product_type' : Select(attrs = {'class':'form-control input-sm', 'onchange':'show_bundle($(this))'}, choices = items_constant.PRODUCT_TYPE),
            'sku' : TextInput(attrs = {'class':'form-control input-sm',}),
            'product_name' : TextInput(attrs = {'class':'form-control input-sm',}),            
            'product_description' : Textarea(attrs = {'class':'form-control input-sm',}),
            'cost_price' : NumberInput(attrs = {'class':'form-control input-sm',}),            
            'selling_price' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'discount' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'tax' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'gst' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'hsn_code' : TextInput(attrs = {'class':'form-control input-sm',}),
            'abatement' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'unit' : Select(attrs = {'class':'form-control input-sm',}, choices = items_constant.UNITS),           
            'purchase_account' : Select(attrs = {'class':'form-control input-sm',},),
            'sales_account' : Select(attrs = {'class':'form-control input-sm',},),
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
            'product_image' : FileInput(attrs = {'class':'form-control input-sm', 'id':'files','name':'files[]','type':'file','multiple' : 'true', 'accept':'image/jpeg, image/png, image/gif,',})
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

#==================================================================================
# BUNDLE EDIT PRODUCT FORM
#==================================================================================
#

class BundleProductForm(ModelForm):

    def __init__(self, user, inv, *args, **kwargs):
        self.user = user
        super(BundleProductForm, self).__init__(*args, **kwargs)
        
        # Exclude product, if already assigned to the bundle instance
        #
        products_in_inv = BundleProducts.objects.filter(product_bundle_id = inv)

        self.fields['product'].queryset = ProductsModel.objects.filter(user = self.user).exclude(pk__in = products_in_inv)
        

    class Meta:
        model = BundleProducts

        fields = ('product','quantity',)

        widgets = {
            'product_type' : Select(attrs = {'class':'form-control input-sm', 'id':'bundle_product_type'}),
            'product' : Select(attrs = {'class':'form-control input-sm'}),
            'quantity' : NumberInput(attrs = {'class':'form-control input-sm'}),
        }