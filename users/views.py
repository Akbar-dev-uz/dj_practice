from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from store.models import Product
from .forms import UserLoginForm, CustomUserCreationForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"{user.username} username li foydalanuvchi yaratildi!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def logout_then_login(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def start_profile(request):
    return render(request, 'users/profile.html')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated your profile!")
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)


@login_required(login_url='login')
def user_products(request):
    user = request.user
    products = Product.objects.filter(owner=user).all()
    context = {'products': products}
    return render(request, 'users/user_products.html', context=context)
