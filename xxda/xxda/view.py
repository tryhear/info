from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
    context = {}
    context['hello'] = '你好，世界！'
    return HttpResponseRedirect('/admin/cjda/')
