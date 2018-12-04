from django.contrib import admin
from website.models import Expense
from website.models import Income


# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)
