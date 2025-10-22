"""
URL configuration for goletan1am project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from goletan1am import index


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index.loginPage, name='loginPage'),
    path('employeesinfo', index.employeesInfoPage, name='employeesInfoPage'),
    path('menu', index.menuPage, name='menuPage'),
    path('payment', index.paymentPage, name='paymentPage'),
    path('history', index.orderHistoryPage, name='orderHistoryPage'),
    path('signup', index.signupPage, name='signupPage'),
    path('customer', index.customerInfoPage, name='customerInfoPage'),
    path('product', index.productPage, name='productPage'),
    path('delivery', index.deliveryPage, name='deliveryPage'),
    path('sales', index.salesPage, name='salesPage'),
    path('supply', index.supplyPage, name='supplyPage'),
    path('about', index.aboutPage, name='aboutPage'),
    path('employee-info/', index.employeesInfoPage, name='employee_info'),
    path('employee-info/delete/<int:employee_id>/', index.delete_employee, name='delete_employee'),
    path('customer/delete/<int:customer_id>/', index.delete_customer, name='delete_customer'),
    path('delivery/delete/<int:delivery_id>/', index.delete_delivery, name='delete_delivery'),
    path('delete-payment/<int:payment_id>/', index.delete_payment, name='delete_payment'),
    path('delete-order/<int:order_id>/', index.delete_order, name='delete_order'),
    path('delete-supply/<int:supply_id>/', index.delete_supply, name='delete_supply'),
    path('login/', index.login_view, name='login_view'),
    path('register/', index.register_view, name='register_view'),
    path('logout/', index.logout_view, name='logout_view'),
    path('delete-sale/<int:sale_id>/', index.delete_sale, name='delete_sale'),
    path('update_delivery_status/<int:delivery_id>/', index.update_delivery_status, name='update_delivery_status'),
]

