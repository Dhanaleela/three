from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'a':20,}
    return render(request,'wish.html',context=d)
def ifelse(request):
    d={'a':10,'b':20}
    return render(request,'ifelse.html',context=d)
def if_elif(request):
    d={'a':25,'b':50,'c':70}
    return render(request,'if_elif.html',d)
def nested(request):
    d={'m':30,'n':20,'o':5}
    return render(request,'nested.html',d)


