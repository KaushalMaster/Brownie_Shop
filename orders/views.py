from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products, registerOrders
from datetime import datetime as d
# Create your views here.


def login(request):
    return render(request, 'templates/login.html')


def signup(request):
    return render(request, 'templates/SignUp.html')


def index(request):
    products = Products.objects.all()
    return render(request, 'templates/index.html', {'Products': products})


def shop_details(request):
    # eid = Product_details.objects.get(P_id=myid)
    # data = Products.objects.filter(eid=eid).order_by('-id')
    # ans = Product_details.objects.get(id=myid)
    # print(ans)
    d = {
        'one': 'shop_details/1',
        'two': 'shop_details/2'
    }
    return render(request, 'templates/shop-details.html')


def contact(request):
    return render(request, 'templates/contact.html')


@ login_required(login_url='login')
def checkout(request):
    return render(request, 'templates/checkout.html')


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        brownie = request.POST.get('brownie')
        quantity = request.POST.get('quantity')
        date = d.now()
        print(full_name, email, brownie, quantity)

        ans = registerOrders(full_name=full_name, email=email,
                             brownie=brownie, quantity=quantity, date=date)
        ans.save()
        return redirect(index)
    return render(request, 'register.html')


def home(request):
    return render(request, 'templates/index.html')
