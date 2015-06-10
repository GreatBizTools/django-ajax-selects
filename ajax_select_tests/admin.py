from django.contrib import admin

from ajax_select.admin import AjaxSelectAdmin

from .models import TestUser

@admin.register(TestUser)
class TestUserAdmin(AjaxSelectAdmin):
    pass