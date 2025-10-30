from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


# Create your views here.

@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    search = request.GET.get('products_search')
    if search:
        products = products.filter(title__icontains=search)
    context = {
        "products": products,
    }
    return render(request, 'store/home.html', context=context)


@login_required(login_url='login')
def view(request, product_id):
    context = {
        'product': Product.objects.get(id=product_id)
    }
    return render(request, 'store/view.html', context=context)


@login_required(login_url='login')
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            messages.success(request, "Продукт успешно создан!")
        return redirect('home')
    else:
        form = ProductForm()
        return render(request, 'store/create.html', {'form': form})


@login_required(login_url='login')
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, message=f"{product.title} o'zgartirildi!")
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'store/update.html', context)


@login_required(login_url='login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')


