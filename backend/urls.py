"""
URL configuration for goletan1am project.

Public views (login, register) come from backend.index.
Protected views (menu, pages) come from members.views with @login_required.
"""

from django.contrib import admin
from django.urls import path
from backend import index          # ✅ keeps your data management + logic views
from members import views          # ✅ protected menu and page views

urlpatterns = [
    # --- Admin ---
    path('admin/', admin.site.urls),

    # --- Public / Authentication Routes ---
    path('', index.loginPage, name='loginPage'),
    path('login/', index.login_view, name='login_view'),
    path('logout/', index.logout_view, name='logout_view'),
    path('register/', index.register_view, name='register_view'),
    path('signup/', index.signupPage, name='signupPage'),

    # --- Protected Routes (Require Login) ---
    path('menu/', views.menu_view, name='menu'),                       # 🔒 protected
    path('employeesinfo/', views.employees_view, name='employeesinfo'),# 🔒 protected
    path('history/', views.history_view, name='history'),              # 🔒 protected
    path('payment/', views.payment_view, name='payment'),              # 🔒 protected
    path('customer/', views.customer_view, name='customer'),           # 🔒 protected
    path('product/', views.product_view, name='product'),              # 🔒 protected
    path('about/', views.about_view, name='about'),                    # 🔒 protected

    # --- Data Operations (Still from backend.index) ---
    path('employee-info/', index.employeesInfoPage, name='employee_info'),
    path('employee-info/delete/<int:employee_id>/', index.delete_employee, name='delete_employee'),
    path('customer/delete/<int:customer_id>/', index.delete_customer, name='delete_customer'),
    path('delivery/delete/<int:delivery_id>/', index.delete_delivery, name='delete_delivery'),
    path('delete-payment/<int:payment_id>/', index.delete_payment, name='delete_payment'),
    path('delete-order/<int:order_id>/', index.delete_order, name='delete_order'),
    path('delete-supply/<int:supply_id>/', index.delete_supply, name='delete_supply'),
    path('delete-sale/<int:sale_id>/', index.delete_sale, name='delete_sale'),
    path('update_delivery_status/<int:delivery_id>/', index.update_delivery_status, name='update_delivery_status'),

    # --- Reports / Misc ---
    path('sales/', index.salesPage, name='sales'),
    path('supply/', index.supplyPage, name='supply'),
    path('delivery/', index.deliveryPage, name='delivery'),
]
