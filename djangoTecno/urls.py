"""
URL configuration for djangoTecno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from employees.views import (
    home, signup, signout, signin,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
)
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),

    # Empleados usando CBVs
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('create_employee/', EmployeeCreateView.as_view(), name='create_employee'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='update_employee'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='delete_employee'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
