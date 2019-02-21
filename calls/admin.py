from django.contrib import admin
from .models import Contact, Call, Tag, Subject
# Register your models here.
admin.site.register(Contact)
admin.site.register(Call)
admin.site.register(Tag)
admin.site.register(Subject)