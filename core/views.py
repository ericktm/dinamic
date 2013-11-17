from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from core.models import Contact


def index(request):
    return render_to_response('layout.html')


def get_data(request):
    record_list = Contact.objects.all()

    data_return = dict()
    data_return['sEcho'] = '1'
    data_return['iTotalRecords'] = str(record_list.count())

    data_return['aaData'] = {}
    for item in record_list.values_list():
        data_return['aaData'][''] = 'fwfe'

    print data_return
    json = serializers.serialize('json', record_list)
    return HttpResponse(json, mimetype='text/json')
