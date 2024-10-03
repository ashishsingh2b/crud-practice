from django.shortcuts import render,redirect,get_object_or_404
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_restro(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirect after successful save
    else:
        form = RestaurantForm()  # Empty form for GET requests

    return render(request, 'addrestaurant.html', {'form': form})


def list_restro(request):
    restaurants= Restaurant.objects.all()
    return render(request,'listrestaurant.html',{'restaurants':restaurants})

def update_restro(request,id):  # Add 'id' as a parameter
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == "POST":
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'updaterestaurant.html', {'form': form})

def delete_restro(request,id):
    restaurant=get_object_or_404(Restaurant,id=id)
    if request.method=="POST":
        restaurant.delete()
        return redirect('list')
    return render(request,'listrestaurant.html')