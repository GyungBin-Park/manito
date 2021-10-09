from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(db_jisu)
admin.site.register(stock_info)
admin.site.register(db_interaction)
admin.site.register(kospi200_list)