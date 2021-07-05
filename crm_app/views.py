from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import Slider
from prices.models import CardPrice, TablePrice
from telebot.sendmessage import send_telegramm

def first_page(request):
    cp1 = CardPrice.objects.get(pk=1)
    cp2 = CardPrice.objects.get(pk=2)
    cp3 = CardPrice.objects.get(pk=3)
    table_prices = TablePrice.objects.all()
    sliders = Slider.objects.all()
    form = OrderForm()
    dict = {'sliders': sliders,
            'cp1': cp1,
            'cp2': cp2,
            'cp3': cp3,
            'table_prices': table_prices,
            'form': form
            }
    return render(request, './index.html', dict)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        send_telegramm(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {'name': name, 'phone': phone})
    else:
        return render(request, './thanks.html')