from django.shortcuts import render,redirect
from main.forms import GearEntryForm
from main.models import GearEntry
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    gear_entries = GearEntry.objects.all()

    context = {
        'npm' : '2306240162',
        'name': 'Farhan Adelio',
        'class': 'PBP C',
        'gear_entries': gear_entries
    }

    return render(request, "main.html", context)

def create_gear_entry(request):
    form = GearEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_gear_entry.html", context)

def show_xml(request):
    data = GearEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GearEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = GearEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = GearEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

