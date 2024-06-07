from django.views.generic import TemplateView, ListView
from .models import Product, Home_products, home_picture, contact_info, about_team
from .forms import ContactForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product.html'


class Home_productListView(ListView):
    model = Home_products
    context_object_name = 'home_products'
    template_name = 'home.html'


class home_pictureListView(ListView):
    model = home_picture
    context_object_name = 'homee'
    template_name = 'home.html'


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'contact.html', context=context)


class contact_infoListView(ListView):
    model = contact_info
    context_object_name = 'contact_info'
    template_name = 'contact.html'


class about_infoListView(ListView):
    model = about_team
    context_object_name = 'about_team'
    template_name = 'about.html'


# ---------------------------------------------------------------------------------------------------------
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)

# --------------------------------------------------------------------------------------------------------
