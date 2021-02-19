from django.contrib import admin
def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_wash:order_list')

    return render(request, 'order_form.html', {'form': form})

from .models import Ticket, Order

admin.site.register(Ticket)
admin.site.register(Order)
