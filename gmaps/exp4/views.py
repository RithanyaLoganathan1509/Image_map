from django.shortcuts import render
def maps(request):
    return render(request,'image.html')
def sar(request):
    return render(request,'saravana.html')
def grtjewel(request):
    return render(request,'grt.html')
def geet(request):
    return render(request,'geetham.html')
def bat(request):
    return render(request,'bata.html')

