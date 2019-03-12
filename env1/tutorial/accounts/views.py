from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Pham Hai An'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
