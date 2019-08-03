from django.contrib import admin
from spendwise.models import Transaction, Region, Tag

admin.site.register(Region)
admin.site.register(Tag)
admin.site.register(Transaction)
