from django.shortcuts import render, redirect
from .forms import GuestEmailForm
from .models import User

def sign(request):
  if request.method == 'POST':
    form = GuestEmailForm(request.POST)

    if form.is_valid():
      new_guest = User(full_name=request.POST['fullname'], email=request.POST['email'], username=request.POST['username'])
      new_guest.save()
      return redirect('eshop:home')

  else:
    form = GuestEmailForm()

  context = {'form': form}
  return render(request, 'account/sign.html', context)

def log(request):
  
  return render(request, 'account/login.html')