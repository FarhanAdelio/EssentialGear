import datetime
from django.shortcuts import render,redirect
from main.forms import GearEntryForm
from main.models import GearEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


@login_required(login_url='/login')
def show_main(request):

    context = {
        'name': request.user.username,
        'npm' : '2306240162',
        'class': 'PBP C',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_gear_entry(request):
    form = GearEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        gear_entry = form.save(commit=False)
        gear_entry.user = request.user
        gear_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_gear_entry.html", context)

def show_xml(request):
    data = GearEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GearEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = GearEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = GearEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        messages.error(request, "Invalid username or password. Please try again.")
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_gear(request, id):
    gear = GearEntry.objects.get(pk = id)
    form = GearEntryForm(request.POST or None, instance=gear)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_gear.html", context)

def delete_gear(request, id):
    gear = GearEntry.objects.get(pk = id)
    gear.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# {% comment %} name = models.CharField(max_length=255)
#     price = models.IntegerField()
#     description = models.TextField(max_length=300)
#     stock = models.IntegerField()
#     rating = models.IntegerField() {% endcomment %}
@csrf_exempt
@require_POST
def add_gear_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = strip_tags(request.POST.get("price")) # strip HTML tags!
    description = request.POST.get("description")
    stock = request.POST.get("stock")
    rating = request.POST.get("rating")
    user = request.user


    new_gear = GearEntry(
            name=name, 
            price = price,
            description=description,
            stock=stock,
            rating=rating,
            user = request.user
    )

    new_gear.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_gear_flutter(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            
            # Create a new Product object
            new_gear = create_gear_flutter(
                user=request.user,  # Ensure the user is authenticated
                name=data["name"],
                price=int(data["price"]),
                description=data["description"],
                stock=data["stock"],
                rating=data["rating"],
            )
            
            # Save the product object
            new_gear.save()

            return JsonResponse({"status": "success"}, status=200)
        except KeyError as e:
            return JsonResponse({"status": "error", "message": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)