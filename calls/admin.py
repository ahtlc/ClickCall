from django.contrib import admin
from .models import Contact, Call, Tag, Subject

admin.site.register(Contact)
admin.site.register(Call)
admin.site.register(Tag)
admin.site.register(Subject)
admin.site.site_header = "Clickcall"