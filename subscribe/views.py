from django.shortcuts import render


def subs(request):
    return render(request,'subscribe/sub.html')
