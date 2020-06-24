from django.shortcuts import render
from django.db import models
from django.contrib import admin
from django.apps import apps as cache
from django.core.management import call_command
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils.module_loading import import_module

import json
from importlib import reload

# Create your views here.
@csrf_exempt
def create_dynamic_tables(request):
    """
    attrs : [
        {"field_type": "int", "field_name": "Age"},
        {"field_type": "char", "field_name": "Name"},
    ]
    """
    req_attrs = request.POST.get('attrs', None)
    table_name = request.POST.get('table_name',None)

    print (req_attrs, type(req_attrs))
    print (table_name)

    try:
        req_attrs = json.loads(req_attrs)
    except Exception as e:
        print (e)
        return JsonResponse({'message': "Invalid request parameter"},status=400)

    attrs = {
        '__module__': 'usertables.models'
    }

    for attr in req_attrs:
        if attr['field_type'] == 'int':
            attrs[attr['field_name']] = models.IntegerField(null=True, blank=True)
        else:
            attrs[attr['field_name']] = models.CharField(max_length=100,null=True,blank=True,default=None)
    
    modl = type(table_name, (models.Model,), attrs)

    call_command('makemigrations')
    call_command('migrate',interactive=False)

    print (settings.BASE_DIR + '/usertables/manage.py')
    
    with open(settings.BASE_DIR + '/usertables/models.py','w') as f:
        call_command('inspectdb',stdout=f)

    admin.site.register(modl)
    reload(import_module(settings.ROOT_URLCONF))

    return JsonResponse({'message': 'Successfully executed'})