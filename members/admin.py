from django.contrib import admin
from .models import Member
from .models import Customer
from .models import Delivery
from .models import Payment
from .models import Order
from .models import Supply
from .models import SalesReport

admin.site.register(Member)
admin.site.register(Customer)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Supply)
admin.site.register(SalesReport)