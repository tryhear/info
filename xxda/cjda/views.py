from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators import csrf
# from cjda.models import test1

# Create your views here.
def index(request):
    context = {}
    context['hello'] = '你好，CJDA！'
    return render(request, 'cjda/hello.html', context)

'''
def testdb(request):
    response = ''
    response1 = ''
    list = test1.objects.all()
    response2 = test1.objects.filter(id=1)
    response3 = test1.objects.get(id=1)
    test1.objects.order_by('name')[0:2]
    test1.objects.order_by('id')
    test1.objects.filter(name='runoob').order_by('id')
    for var in list:
        response1 += var.name + ' '
    response = response1
    return HttpResponse('<p>' + response + '</p>')

    # test1=test(name='runoob')
    # test1.save()
    # return HttpResponse('<p>ok!</p>')
'''


def search_form(request):
    return render_to_response('cjda/search_form.html')


def search(request):
    # request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'your search message is:' + request.GET['q']
    else:
        message = 'You post none'
    return HttpResponse(message)


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, 'cjda/post.html', ctx)

