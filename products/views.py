from django.shortcuts import render
from .models import decorationlist 
def decorationslist(request):
    data=decorationlist.objects.all()
    content={'data': data}
    return render(request,'products.html',context=content)

