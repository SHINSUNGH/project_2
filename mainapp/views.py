from django.shortcuts import render
from django.http import HttpResponse


# 최초 인덱스 페이지
def index(request):
    return render(request, 'mainapp\index.html', {})

# main 페이지
def main(request):
    return render(request, 'mainapp\index.html', {})

# reference 페이지
def reference(request):
    return render(request, 'mainapp/reference/index.html', {})