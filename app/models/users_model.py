from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

from app.models.contacts_model import *

#**************************************************************************
#   USER'S PROFILE DETAILS
#**************************************************************************
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index = True,)
    
    app_id = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    salutation = models.IntegerField(
        db_index = True,
        default = 0,
        choices = user_constants.SALUTATIONS,
        blank = True,
    )

    customer_type = models.IntegerField(
        db_index = True,
        choices = user_constants.CUSTOMER_TYPE,
        default = 1,
        blank = True,
    )

    official_phone = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    personal_phone = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    display_name = models.CharField(
        max_length = 250,
        blank = False,
        db_index = True,
        null = True,
    )

    organization_type = models.IntegerField(
        db_index = True,
        choices = user_constants.ORGANIZATION_TYPE,
        default = 1,
    )

    organization_name = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    website = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'user_profile_tbl'

#**************************************************************************
#   USER'S ACCOUNT DETAILS
#**************************************************************************
class User_Account_Details(models.Model):

    is_user = models.BooleanField(
        default = False,
        db_index = True,
        choices = user_constants.IS_TRUE,
    )

    user = models.ForeignKey(
        User,
        blank = True,
        null = True, 
        on_delete = models.CASCADE,
        db_index = True,
    )

    contact = models.ForeignKey(
        Contacts,
        db_index = True,
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )

    account_number = models.CharField(
        max_length = 30,
        blank = True,
        db_index = True,
        null = True,
    )

    account_holder_name = models.CharField(
        max_length = 250,
        blank = True,
        db_index = True,
        null = True,
    )

    ifsc_code = models.CharField(
        max_length = 20,
        blank = True,
        db_index = True,
        null = True,
    )

    bank_name = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    bank_branch_name = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
        null = True,
    )

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    class Meta:
        verbose_name_plural = 'user_account_details_tbl'


#**************************************************************************
#   EMAIL ADDRESSES OF CONTACTS
#   A CONTACT/USER CAN HAVE MULTIPLE MAIL ADDRESSES
#**************************************************************************
class User_Email_Details(models.Model):

    is_user = models.BooleanField(
        default = False,
        db_index = True,
        choices = user_constants.IS_TRUE,
    )

    user = models.ForeignKey(
        User,
        blank = True,
        null = True, 
        on_delete = models.CASCADE,
        db_index = True,
    )

    contact = models.ForeignKey(
        Contacts,
        db_index = True,
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )
    
    email = models.EmailField(
        blank = False, 
        null = True, 
        db_index = True,
    )

    is_official = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = True,
    )

    is_personal = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
        null = True,
    )

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    def is_official_full(self):
        if self.is_official:
            return "YES"
        return "NO" 

    def is_personal_full(self):
        if self.is_personal:
            return "YES"
        return "NO" 

    class Meta:
        verbose_name_plural = 'user_email_tbl'


#**************************************************************************
#   ADDRESSES OF USERs
#   A User CAN HAVE MULTIPLE ADDRESSES
#**************************************************************************

class User_Address_Details(models.Model):

    is_user = models.BooleanField(
        db_index = True,
        default = False,
        choices = user_constants.IS_TRUE,
    )

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    contact = models.ForeignKey(
        Contacts,
        db_index = True,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    contact_person = models.CharField(
        blank = True,
        null = True,
        max_length = 250,
    )

    flat_no = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    street = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    city = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    state = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
        choices = country_list.STATE_LIST_CHOICES,
    )

    country = models.CharField(
        max_length = 5,
        blank = True,
        null = True,
        db_index = True,
        choices = country_list.COUNTRIES_LIST_CHOICES,
        default = 'IN',
    )

    pincode = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    is_billing_address_diff = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = False,
    ) 
    
    is_billing_address = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = False,
    ) 

    is_shipping_address = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
        null = True,
    )

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    def __str__(self):
        return self.flat_no +", "+self.street+", "+self.city

    def complete_billing_address(self):
        return self.flat_no +", "+self.street

    def is_billing_address_full(self):
        if self.is_billing_address:
            return "YES"
        return "NO"

    def is_shipping_address_full(self):
        if self.is_shipping_address:
            return "YES"
        return "NO"

    def same_billing_shipping_address_full(self):
        if self.is_billing_address == self.is_shipping_address:
            return "YES"
        return "NO"

    class Meta:
        verbose_name_plural = 'user_address_details_tbl'


#**************************************************************************
#   Tax Details OF users
#   A user CAN HAVE only one tax detail
#**************************************************************************

class User_Tax_Details(models.Model):
    
    is_user = models.BooleanField(
        db_index = True,
        default = False,
        choices = user_constants.IS_TRUE,
    )

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    contact = models.ForeignKey(
        Contacts,
        db_index = True,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    pan = models.CharField(
        max_length = 10,
        db_index = True,
        blank = True,
        null = True,
    )

    gstin = models.CharField(
        max_length = 100,
        db_index = True,
        blank = True,
        null = True,
    )

    gst_reg_type = models.IntegerField(
        db_index = True,
        default = 0,
        choices = user_constants.GST_REG_TYPE,
        blank = True,
        null = True,
    )

    business_reg_no = models.CharField(
        max_length = 15,
        blank = True,
        null = True,
        db_index = True,
    )

    tax_reg_no = models.CharField(
        max_length = 15,
        blank = True,
        null = True,
        db_index = True,
    )

    cst_reg_no = models.CharField(
        max_length = 15,
        blank = True,
        null = True,
        db_index = True,
    )

    tds = models.DecimalField(
        db_index = True,
        null = True,
        blank = True,
        max_digits = 20, 
        decimal_places = 2
    )

    preferred_currency = models.CharField(
        max_length = 5,
        db_index = True,
        default="INR",
        choices = currency_list.CURRENCY_CHOICES,
        blank = True,
        null = True,
    )

    opening_balance = models.IntegerField(
        blank = True,
        null = True,
        db_index = True,
        default = 0.00,
    )

    as_of = models.DateTimeField(
        auto_now = True,
        db_index = True,
        null = True,
    )

    preferred_payment_method = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = payment_constants.PREFERRED_PAYMENT_TYPE,
        default = 0
    )

    preferred_delivery = models.IntegerField(
        default = 0,
        db_index = True,
        choices = payment_constants.PREFERRED_DELIVERY,
        null = True,
        blank = True,
    )

    invoice_terms = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = payment_constants.PAYMENT_DAYS,
    )

    bills_terms = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = payment_constants.PAYMENT_DAYS,
    )

    class META:
        verbose_name_plural = 'user_tax_details_tbl'


#==================================================================
# Create instances on User Creation
#==================================================================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        pro = Profile.objects.create(user=instance)
        pro.app_id = 'APK-'+get_random_string(length=10)
        pro.save()

