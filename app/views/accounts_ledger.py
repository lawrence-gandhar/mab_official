from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from collections import OrderedDict, defaultdict
from django.db.models import *


from app.models import *
from app.forms import *
from app.other_constants import *

import json

#
#
#
def get_predefined_groups(request):
    
    htm = ['<option value="">-----</option>']

    if request.GET:

        for i,v  in accounts_constant.ACCOUNTS_LEDGER_GROUPS_DICT[int(request.GET["ids"])].items():
            htm.append('<option value="{}">{}</option>'.format(i,v))
        
        #
        # GET ITEMS FOR DB AND APPEND TO STANDARD LIST 
        acc_group = accounts_model.AccGroups.objects.filter(major_head = int(request.GET["ids"]), user = request.user, is_active = True)
        
        grp = request.GET["ids"]+'-'+str(request.user.id)+"-"
        for acc in acc_group:
            htm.append('<option value="{}{}">{}</option>'.format(grp,acc.id, acc.group_name))
            
    htm.append('<option style="background-color:#913f9e; color:#FFFFFF" value="-1">+ New Group</option>')
    return HttpResponse(''.join(htm))



#
#
#
class AccLedger(View):
    
    # Template 
    template_name = 'app/app_files/acc_ledger/index.html'

    data = defaultdict()

    data["included_template"] = 'app/app_files/acc_ledger/add_accounts_ledger.html'

    data["css_files"] = []
    data["js_files"] = ['custom_files/js/ledger.js']

    data["active_link"] = 'Accounts'
    
    #
    #
    def get(self, request):

        self.data["ledger_form"] = accounts_ledger_forms.AccLedgerForm()
        self.data["groups_form"] = accounts_ledger_forms.AccGroupsForm()
        return render(request, self.template_name, self.data)

    #
    #
    def post(self, request):
        ledger_form = accounts_ledger_forms.AccLedgerForm(request.POST)

        if ledger_form.is_valid():
            obj = ledger_form.save(commit = False)
            obj.user = request.user
            obj.save()

        return redirect('/ledger/add/', permanent = False) 

#
#
#
def add_ledger_group(request):
    if request.POST:
        groups_form = accounts_ledger_forms.AccGroupsForm(request.POST)

        if groups_form.is_valid():
            obj = groups_form.save(commit = False)
            obj.user = request.user
            obj.major_head = int(request.POST["ids"])
            obj.save()

            grp = request.POST["ids"]+'-'+str(request.user.id)+"-"+str(obj.id)
            return HttpResponse(grp)
        return HttpResponse('0')
    return HttpResponse('0')