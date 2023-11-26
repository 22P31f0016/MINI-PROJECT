from django.shortcuts import render
from .models import orderlist
def orderslist(request):
    data=orderlist.objects.all()
    content={'data':data}
    return render(request,'orders.html',context=content)
