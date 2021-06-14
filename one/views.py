from django.shortcuts import render,redirect
from .models import product, incart , Category
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#####################################
def customer(request):
    products = product.objects.all()
    if 'catid' in request.GET.keys():
        products = product.objects.filter(category = Category.objects.get(id = request.GET['catid']))
    elif request.user.is_authenticated and request.GET:
        pk = request.GET['id']
        ch = product.objects.get(id=pk)
        llist = [i for i in incart.objects.filter(choise = ch ,username = request.user)]
        if llist:
            for i in llist:
                if product.objects.get(id=pk).quantity > 0:
                    if incart.objects.get(choise = product.objects.get(id = pk), username = request.user).quantity >= product.objects.get(id=pk).quantity:
                        messages.info(request , 'Taklif soni cheklangan!')
                    else:
                        incart.objects.filter(choise = i.choise ,username = request.user).update(quantity = int(i.quantity) + 1)
                        messages.info(request, 'Muvaffaqiyatli qo`shildi')
        else:
            cart = incart(username = request.user , choise=ch,quantity = 1)
            messages.info(request, 'Muvaffaqiyatli qo`shildi')
            cart.save()
        return redirect('customer')
    categories = Category.objects.all()
    mychoices = incart.objects.filter(username=request.user)
    context = {
        'categories':categories,
        'products':products,
        'mychoices':mychoices,
    }
    return render(request , 'customer.html',context)
def productView(request, pk):
    mychoices = incart.objects.filter(username=request.user)
    pro = product.objects.get(id = pk)
    return render(request , 'detail.html' , {'product':pro,'mychoices':mychoices,})
def basket(request):
    if request.GET:
        pn = request.GET['id']
        if request.GET['quantity'] == 'up':
            if incart.objects.get(id = pn,username = request.user).choise.quantity > 0:
                if incart.objects.get(id = pn,username = request.user).quantity >= incart.objects.get(id = pn,username = request.user).choise.quantity:
                    pass
                else:
                    incart.objects.filter(id=pn,username = request.user).update(quantity= (incart.objects.get(id = pn,username = request.user).quantity) + 1)
            else:
                pass
        if request.GET['quantity'] == 'down':
            if incart.objects.get(id = pn,username = request.user).quantity <= 1:
                incart.objects.filter(id=pn,username = request.user).delete()
            else:
                incart.objects.filter(id=pn,username = request.user).update(quantity= (incart.objects.get(id = pn,username = request.user).quantity) - 1)
        if request.GET['quantity'] == 'delete':
            incart.objects.filter(username=request.user , id = pn).delete()
        return redirect('basket')
    mychoices = incart.objects.filter(username = request.user)
    allprice = 0
    for i in mychoices:
        allprice += float(i.choise.price) * int(i.quantity)
    context = {
        'mychoices':mychoices,
        'total': allprice,
        'add':'add',
        'multiplication':'multiplication',
    }
    return render(request , 'basket.html',context)
########################3
def signupPage(request):
    form = CreateUserForm()
    if request.method == "POST":

            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    return render(request,'signup.html',{'form':form,})
def loginPage(request):
    if request.method == "POST":
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('customer')
        else:
            messages.info(request, 'Username yoki Parol xato')
    return render(request, 'login.html',{})
def logoutPage(request):
    if request.method == "POST":
        incart.objects.filter(username = request.user).delete()
        logout(request)
        return redirect('customer')
    return render(request, 'logout.html')

#############################################
def tolov(request):
    return render(request , 'tolov/pay.html' , {})