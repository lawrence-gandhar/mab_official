from django.db import models
from django.contrib.auth.models import User
from app.other_constants import state_list
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models.users_model import *
from app.models.items_model import *
from app.models.contacts_model import *

from uuid import uuid4
import os


#**************************************************************************
#   CREDITNOTE'S DATA
#**************************************************************************
class CreditNode(models.Model):
  

    user = models.ForeignKey(User, on_delete = models.CASCADE, db_index = True, null = True,)

    service_recipient = models.ForeignKey(
        Contacts, 
        on_delete = models.SET_NULL, 
        db_index = True,
        null = True,
        blank = True,
    )

    state = models.CharField(
        max_length = 2,
        db_index = True,
        choices = state_list.STATE_LIST_CHOICES
    )

    email = models.EmailField(
        db_index = True,
    )

    billing_address = models.CharField(
        max_length = 500,
        db_index = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    )

    Message_on_customer_statement = models.CharField(
        max_length = 250,
        blank = False, 
        null = True, 
        db_index = True,
    )

    Message_on_credit_note  = models.CharField(
        max_length = 250,
        blank = False, 
        null = True, 
        db_index = True,
    )

    def __str__(self):
        return self.service_recipient 

    class Meta:
        verbose_name_plural = 'creditnote_tbl'
#**************************************************************************
#   ADD ITEM'S DATA
#**************************************************************************

class Items(models.Model):       

    product = models.ForeignKey(
        ProductsModel,
        on_delete = models.SET_NULL,
        db_index = True,
        blank = True,
        null = True,
    )

    inventory = models.ForeignKey(
        InventoryProduct,
        on_delete = models.SET_NULL,
        db_index = True,
        null = True,
        blank = True,
    )

    quantity = models.IntegerField(
        db_index = True,
        null = True,
        blank = True,
    )

    price = models.IntegerField(
        db_index = True,
        null = True,
        blank = True,
    )

    discount = models.FloatField(
        default = 0,
        db_index = True,
    )

    tax = models.FloatField(
        default = 0,
        db_index = True,
    )

    amount = models.FloatField(
        default = 0,
        db_index = True,
    )

    cgst = models.FloatField(
        default = 0,
        db_index = True,
    )

    igst = models.FloatField(
        default = 0,
        db_index = True,
    )

    sgst = models.FloatField(
        default = 0,
        db_index = True,
    )

    adjustment = models.FloatField(
        default = 0,
        db_index = True,
    )

    total = models.FloatField(
        default = 0,
        db_index = True,
    )
    
    def __str__(self):
        return self.product 

    class Meta:
        verbose_name_plural = 'creditnote_item_tbl'