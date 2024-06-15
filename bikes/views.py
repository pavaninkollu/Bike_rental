from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike, Rental
from django.contrib.auth.decorators import login_required
from .forms import BikeForm

# Create your views here.


def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/bike_list.html', {'bikes': bikes})

@login_required
def rent_bike(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    if bike.available:
        Rental.objects.create(user=request.user, bike=bike)
        bike.available = False
        bike.save()
        return redirect('bike_list')
    return render(request, 'bikes/rent_bike.html', {'bike': bike, 'error': 'Bike not available'})




@login_required
def add_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'bikes/add_bike.html', {'form': form})


@login_required
def delete_bike(request,bike_id):
    bike=get_object_or_404(Bike,id=bike_id)
    bike.delete()
    return redirect('bike_list')