from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse, reverse_lazy
from .forms import *
from .models import Item, Vendor
from django.views.generic import *


# Create your views here.

#############################
#       HOME VIEW          #
#############################
def cim_home(request):
    return render(request, 'cim_home.html', {})


#############################
#       ITEMS VIEW          #
#############################

class ListItemsView(ListView):
    model = Item
    template_name = 'cim_list.html'


class DetailItemView(DetailView):
    model = Item
    template_name = 'cim_item.html'


class AddItemView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'cim_new.html'


class UpdateItemView(UpdateView):
    model = Item
    form_class = EditItemForm
    template_name = 'cim_edit.html'


class DeleteItemView(DeleteView):
    model = Item
    template_name = 'cim_delete.html'
    success_url = reverse_lazy('cim_list')


#############################
#       VENDOR VIEW         #
#############################


class ListVendorView(ListView):
    model = Vendor
    template_name = 'cim_listVendor.html'


class DetailVendorView(DetailView):
    model = Vendor
    template_name = 'cim_viewVendor.html'


class AddVendorView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'cim_newVendor.html'


class UpdateVendorView(UpdateView):
    model = Vendor
    form_class = EditVendorForm
    template_name = 'cim_editVendor.html'


