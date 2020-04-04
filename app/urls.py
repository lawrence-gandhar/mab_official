from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from app.views import dashboard, contacts, base, invoice, collections, \
    products, inventory, common_views


# Authorization
urlpatterns = [
    path('', dashboard.index, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'app/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'app/registration/logout.html'), name = 'logout'),
    re_path(r'^accounts/*', RedirectView.as_view(pattern_name='login', permanent=True)),
    path('unauthorized/', login_required(base.UnAuthorized.as_view()), name = 'unauthorized'),
    path('signup/', base.signup, name='signup'),
]

# Dashboard
urlpatterns += [
    path('dashboard/', never_cache(login_required(dashboard.Dashboard.as_view())), name = 'dashboard'),
]

# Contacts
urlpatterns += [
    path('contacts/', never_cache(login_required(contacts.ContactsView.as_view())), name = 'contacts'),
    path('contacts/add/', never_cache(login_required(contacts.add_contacts)), name = 'add-contacts'),
    path('contacts/add_address/', never_cache(login_required(contacts.add_address_details_form)), name = 'add_address_details_form'),
    path('contacts/add_accounts/', never_cache(login_required(contacts.add_accounts_details_form)), name = 'add_accounts_details_form'),
    path('contacts/edit/<int:ins>/', never_cache(login_required(contacts.edit_contact)), name = 'edit-contact'),
    
    path('contacts/check_appid/', never_cache(login_required(contacts.check_app_id)), name='check-appid'),
    path('contacts/user_exists_in_list/', never_cache(login_required(contacts.user_exists_in_list)), name='check-appid-user-exist'),
    path('contacts/upload/<str:a>/', never_cache(login_required(contacts.ContactsFileUploadView.as_view())), name='contacts-upload'),
    path('contacts/status_change/<slug:slug>/<int:ins>/', never_cache(login_required(contacts.status_change)), name='contact-status-change'),
    path('contacts/delete/<int:ins>/', never_cache(login_required(contacts.delete_contact)), name='contact-delete'),

    path('contacts/edit_contact_details_form/', never_cache(login_required(contacts.edit_contact_details_form)), name = 'edit_contact_details_form'),
    path('contacts/edit_tax_details_form/', never_cache(login_required(contacts.edit_tax_details_form)), name = 'edit_tax_details_form'),
    path('contacts/edit_other_details_form/', never_cache(login_required(contacts.edit_other_details_form)), name = 'edit_other_details_form'),
    path('contacts/edit_address_details_form/', never_cache(login_required(contacts.edit_address_details_form)), name = 'edit_address_details_form'),
    path('contacts/edit_accounts_details_form/', never_cache(login_required(contacts.edit_accounts_details_form)), name = 'edit_accounts_details_form'),
    path('contacts/edit_social_details_form/', never_cache(login_required(contacts.edit_social_details_form)), name = 'edit_social_details_form'),

    path('contacts/delete_address/<int:ins>/', never_cache(login_required(contacts.delete_contact_address)), name = 'delete_contact_address'),
    path('contacts/delete_accounts/<int:ins>/', never_cache(login_required(contacts.delete_accounts_details)), name = 'delete_accounts_details'),

]

# Invoice
urlpatterns += [
    path('invoice/', never_cache(login_required(invoice.Invoice.as_view())), name = 'invoice'),
    path('invoice/invoice_designer/', never_cache(login_required(invoice.InvoiceDesigner.as_view())), name = 'invoice-designer'),
    path('invoice/invoice_designer/manage/', never_cache(login_required(invoice.manage_invoice_designs)), name = 'manage-invoice-designs'),
    path('invoice/create_invoice/', never_cache(login_required(invoice.CreateInvoice.as_view())), name = 'create-invoice'),
    path('invoice/view_invoice/<int:ins>/', never_cache(login_required(invoice.ViewInvoice.as_view())), name = 'view-invoice'),
    path('invoice/create_invoice/contacts/<int:ins>/', never_cache(login_required(invoice.CreateContactInvoice.as_view())), name = 'create-contact-invoice'),
    path('invoice/create_invoice/collections/<int:ins>/', never_cache(login_required(invoice.CreateCollectionInvoice.as_view())), name = 'create-collection-invoice'),
]

urlpatterns +=[
    path('invoice/get_pdf/<int:ins>/', never_cache(login_required(invoice.get_pdf)), name = 'get_pdf'),
    
] 

# Collections
urlpatterns += [
    path('collections/', never_cache(login_required(collections.view_collections)), name = 'collections'),
    path('collections/contact/<int:ins>/', never_cache(login_required(collections.view_contact_collections)), name = 'contact-collections'),
    path('collections/add_collections/', never_cache(login_required(collections.AddCollections.as_view())), name = 'add-collections'),
    path('collections/add_collections/partial/<int:ins>/', never_cache(login_required(collections.AddPartialCollection.as_view())), name = 'add-partial-collections'),
    path('collections/edit/<int:ins>/', never_cache(login_required(collections.Edit_Collection.as_view())), name = 'edit_collections'),
    path('collections/edit_partial/<int:ins>/<int:obj>/', never_cache(login_required(collections.Edit_PartialCollection.as_view())), name = 'edit_partial_collection'),
]

# Products
urlpatterns += [
    path('products/', never_cache(login_required(products.view_products)), name = 'view_products'),
    path('products/add/', never_cache(login_required(products.AddProducts.as_view())), name = 'add_products'),
    path('products/edit/<int:ins>/', never_cache(login_required(products.EditProducts.as_view())), name = 'edit_product'),
    path('products/delete/<int:ins>/', never_cache(login_required(products.delete_product)), name='product-delete'),
    path('products/status_change/<slug:slug>/<int:ins>/', never_cache(login_required(products.status_change)), name='product-status-change'),
    # BUNDLE ADDED BY ROSHAN
    path('prducts/bundle/',never_cache(login_required(products.bundle)),name='bundle'),
]

# Inventory
urlpatterns += [
    path('inventory/', never_cache(login_required(inventory.view_inventory)), name = 'view_inventory'),
    path('inventory/add/', never_cache(login_required(inventory.AddInventory.as_view())), name = 'add_inventory'),
    path('inventory/products/<int:ins>/', never_cache(login_required(inventory.InventoryProducts.as_view())), name = 'view_inventory_products'),
    path('inventory/products/delete/<int:ins>/', never_cache(login_required(inventory.delete_inventory_product)), name = 'delete_inventory_product'),
    path('inventory/get_edit_inventory_product_form/', never_cache(login_required(inventory.get_edit_inventory_product_form)), name = 'get_edit_inventory_product_form'),
    path('inventory/edit_inventory_product/', never_cache(login_required(inventory.edit_inventory_product)), name = 'edit_inventory_product'),
]

# AJAX
urlpatterns += [
    path('fetch_contact_addresses/<int:ins>/', never_cache(login_required(common_views.fetch_contact_addresses)), name='fetch_contact_addresses'),
    path('fetch_product_details/<int:ins>/', never_cache(login_required(common_views.fetch_product_details)), name='fetch_product_details'),
    path('ajax_add_product/', never_cache(login_required(products.ajax_add_product)), name='ajax_add_product'),
    path('fetch_products_dropdown/', never_cache(login_required(common_views.fetch_products_dropdown)), name='fetch_products_dropdown'),
    path('add_contact_or_employee/', never_cache(login_required(common_views.add_contact_or_employee)), name='add_contact_or_employee'),
    path('get_contacts_dropdown/', never_cache(login_required(common_views.get_contacts_dropdown)), name='get_contacts_dropdown'),
    path('add_edit_address/<int:ins>/', never_cache(login_required(common_views.add_edit_address)), name='add_edit_address'),
    path('add_edit_address/<int:ins>/<int:obj>/', never_cache(login_required(common_views.add_edit_address)), name='add_edit_address'),
]





#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()



