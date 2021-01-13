from django.shortcuts import render
from .models import Order, Product

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0

    if 'sum' not in request.session:
        request.session['sum'] = 0

    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    product=Product.objects.get(id=request.POST["id"])
    quantity_from_form = int(request.POST["quantity"])

    price_from_form = float(product.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    context = {
        "charge": total_charge
    }
    request.session["count"]+=1
    request.session["sum"]+=total_charge

    return render(request, "store/checkout.html",context)