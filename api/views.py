from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    
    headers = request.headers
    params = request.GET.get('q')
    post_data = request.body
    
    print(headers)
    print('-------------------------------')
    print(params)
    print('-------------------------------')
    print(post_data)

    
    return JsonResponse({'info':'django api','name':'L14','age':'25 ans','params':params})
    