from django.contrib import admin

from app.models.contacts_model import *
from app.models.invoice_model import *
from app.models.users_model import *
from app.models.collects_model import *
from app.models.items_model import *
# Register your models here.

@admin.register(Contacts)
class C(admin.ModelAdmin):
    model = Contacts

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    model = Profile

@admin.register(User_Account_Details)
class User_Account_Details(admin.ModelAdmin):
    model = User_Account_Details 

@admin.register(User_Address_Details)
class User_Address_Details(admin.ModelAdmin):
    model = User_Address_Details 

@admin.register(InvoiceModel)
class Invoice(admin.ModelAdmin):
    model = InvoiceModel

@admin.register(Collections)
class Collections(admin.ModelAdmin):
    model = Collections

@admin.register(Invoice_Templates)
class Collections(admin.ModelAdmin):
    model = Invoice_Templates

@admin.register(ProductsModel)
class Products(admin.ModelAdmin):
    model = ProductsModel

@admin.register(ProductPhotos)
class ProductPhotos(admin.ModelAdmin):
    model = ProductPhotos

@admin.register(ProductAccounts)
class ProductAccounts(admin.ModelAdmin):
    model = ProductAccounts

    