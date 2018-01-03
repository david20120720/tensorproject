from django.contrib import admin

# Register your models here.

from .models import Game,Question,Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Game)

