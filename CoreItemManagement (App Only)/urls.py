# invoking the name while views.'method' page occurs on browser
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', cim_home, name="cim_home"),

    # Items
    path('items/', ListItemsView.as_view(), name='cim_list'),
    path('additem/', AddItemView.as_view(), name="cim_new"),
    path('item/view/<int:pk>/', DetailItemView.as_view(), name='cim_item'),
    path('item/edit/<int:pk>/', UpdateItemView.as_view(), name="cim_edit"),
    path('item/delete/<int:pk>/', DeleteItemView.as_view(), name="cim_delete"),

    # Vendors
    path('vendors/', ListVendorView.as_view(), name="cim_listVendor"),
    path('addVendor/', AddVendorView.as_view(), name="cim_newVendor"),
    path('vendor/view/<int:pk>/', DetailVendorView.as_view(), name="cim_viewVendor"),
    path('vendor/edit/<int:pk>/', UpdateVendorView.as_view(), name="cim_editVendor"),
]

