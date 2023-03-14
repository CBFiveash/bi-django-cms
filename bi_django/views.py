from django.shortcuts import render
from bi_django.models import Observer


def showdata(request):
    results = Observer.objects.all()
    return render (request, "dbtable_plugin.html", {"data": results})
