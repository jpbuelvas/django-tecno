from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Employess
from .forms import EmployessForm
from django.db.models import Q

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('employees')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm(), "error": "Username already exists."})
        return render(request, 'signup.html', {"form": UserCreationForm(), "error": "Passwords did not match."})

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employess
    template_name = 'employees.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        query = self.request.GET.get('q', '')
        order_by = self.request.GET.get('order_by', 'name')
        print(query, "query")
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(DNI__icontains=query) |
                Q(email__icontains=query)|
                Q(phone__icontains=query)

            )
        return queryset.order_by(order_by)

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employess
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employess
    form_class = EmployessForm
    template_name = 'create_employee.html'
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Esto se mostrará en la consola
        return self.render_to_response(self.get_context_data(form=form, error=form.errors))

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employess
    form_class = EmployessForm
    template_name = 'employee_form.html'  
    success_url = reverse_lazy('employees')
class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employess
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employees')

def home(request):
    return render(request, 'home.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm(), "error": "Username or password is incorrect."})
        login(request, user)
        return redirect('employees')
