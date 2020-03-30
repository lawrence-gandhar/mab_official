from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *
from django.dispatch import receiver

from uuid import uuid4
import os

#==========================================================================
#   CHANGE PRODUCT FILE NAMES
#==========================================================================
#
def product_file_rename(instance, filename):

    upload_path = 'products'
    ext = filename.split('.')[-1]
    return  os.path.join(upload_path,'{}.{}'.format(uuid4().hex, ext))


#=========================================================================================
# INVETORY/STOCK 
#=========================================================================================
#
class Inventory(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    inventory_name = models.CharField(
        max_length = 250,
        db_index = True,
        blank = False,
        null = False,
    )

    in_date = models.DateField(
        null = True,
        blank = True,
        db_index = True,
    )

    stock_cleared = models.BooleanField(
        db_index = True,
        default = False,
        choices = user_constants.IS_TRUE,
    )

    def __str__(self):
        return self.inventory_name.upper()


#=========================================================================================
# PRODUCT SALES/PURCHASE ACCOUNTS
#=========================================================================================
#
class ProductAccounts(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    accounts_name = models.CharField(
        max_length = 250,
        null = False,
        blank = False,
        db_index = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    is_sales = models.BooleanField(
        default = True,
        db_index = True,
        choices = user_constants.IS_TRUE,
    )

    def __str__(self):
        return self.accounts_name.upper()


#=========================================================================================
# ITEMS/PRODUCT MODEL
#=========================================================================================
#
class ProductsModel(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    product_type = models.IntegerField(
        db_index = True,
        default = 0,
        choices = items_constant.PRODUCT_TYPE,
    )

    sku = models.CharField(
        max_length = 20,
        db_index = True,
        null = False,
        blank = False,
    )

    product_name = models.CharField(
        db_index = True,
        blank = False,
        null = False,
        max_length = 250,
    )

    product_description = models.TextField(
        blank = True,
        null = True,
    )

    
    manufactured_date = models.DateField(
        blank = True,
        null = True,
        db_index = True,
    )

    expiry_date = models.DateField(
        blank = True,
        null = True,
        db_index = True,
    )

    product_dimension = models.TextField(
        blank = True,
        null = True,
    )

    cost_price = models.IntegerField(
        default = 0,
        db_index = True,
    )

    marked_price = models.IntegerField(
        default = 0,
        db_index = True,
    )

    selling_price = models.IntegerField(
        db_index = True,
        default = 0,
    )

    discount = models.IntegerField(
        db_index = True,
        default = 0,
    )

    tax = models.IntegerField(
        default = 0.0,
        db_index = True,
        null=True,
        blank=True,
    )

    gst = models.IntegerField(
        default = 0.0,
        db_index = True,
        null=True,
        blank=True,
    )

    hsn_code = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    abatement = models.IntegerField(
        default = 0,
        db_index = True,
    )

    unit = models.IntegerField(
        default = 0,
        db_index = True,
        choices = items_constant.UNITS
    )

    is_sales = models.BooleanField(
        db_index = True,
        default = True,
    )

    is_purchase = models.BooleanField(
        db_index = True,
        default = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    sales_account = models.ForeignKey(
        ProductAccounts,
        on_delete = models.SET_NULL,
        db_index = True,
        related_name = "sales_account",
        null = True,
        blank = True,
    )

    purchase_account = models.ForeignKey(
        ProductAccounts,
        on_delete = models.SET_NULL,
        db_index = True,
        related_name = "purchase_account",
        null = True,
        blank = True,
    )



    def __str__(self):
        return "{} - ({})".format(self.product_name.upper(), self.sku.upper())

#=========================================================================================
# PRODUCT PHOTOS MODEL
#=========================================================================================
#
class ProductPhotos(models.Model):
    product = models.ForeignKey(
        ProductsModel,
        db_index = True,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    product_image = models.FileField(
        upload_to = product_file_rename,
        db_index = True,
        blank = True,
        null = True,
    )

#=========================================================================================
# STOCK PRODUCT COUNTER & NOTIFICATION 
#=========================================================================================
#
class InventoryProduct(models.Model):

    inventory = models.ForeignKey(
        Inventory,
        db_index = True,
        null = True,
        blank = True,
        on_delete = models.CASCADE,
    )

    product = models.ForeignKey(
        ProductsModel,
        db_index = True,
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
    )

    quantity = models.IntegerField(
        db_index = True,
        default = 0,
    )

    unit = models.IntegerField(
        db_index = True,
        blank = True,
        null = True,
        choices = items_constant.UNITS,
    )

    threshold = models.IntegerField(
        default = 0,
        db_index = True,
    )

    stop_at_min_hold = models.IntegerField(
        db_index = True,
        default = 0,
    )

    notify_on_threshold = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    notify_on_min_hold = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    min_hold_date = models.DateField(
        db_index = True,
        null = True,
        blank = True,
    )

    threshold_date = models.DateField(
        db_index = True,
        null = True,
        blank = True,
    )

    min_hold_notify_trigger = models.IntegerField(
        db_index = True,
        null = True,
        blank = True,
        choices = items_constant.PRODUCT_STOCK_NOTIFICATION_TRIGGERS,
    )

    threshold_notify_trigger = models.IntegerField(
        db_index = True,
        null = True,
        blank = True,
        choices = items_constant.PRODUCT_STOCK_NOTIFICATION_TRIGGERS,
    )

    cleared_on = models.DateField(
        db_index = True,
        null = True,
        blank = True,
    )


#=========================================================================================
# STOCK PRODUCT NOTIFICATION REMINDERS 
#=========================================================================================
#    
class InventoryNotificationRemiander(models.Model):

    inventory_product = models.ForeignKey(
        InventoryProduct,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    is_threshold = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    details = models.TextField(
        null = True,
        blank = True,
    )

    created_on = models.DateTimeField(
        auto_now_add = True,
        db_index = True,
    )


#=========================================================================================
# DELETE PRODUCT IMAGES FROM MEDIA ON DELETING A PRODUCT 
#=========================================================================================
#
@receiver(models.signals.post_delete, sender=ProductPhotos)
def image_delete(sender, instance, **kwargs):
    instance.product_image.delete(False)

