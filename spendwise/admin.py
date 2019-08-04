from django.contrib import admin
from spendwise.models import Region, Tag, Place, Transaction

admin.site.register(Region)
admin.site.register(Tag)
admin.site.register(Place)
admin.site.register(Transaction)
