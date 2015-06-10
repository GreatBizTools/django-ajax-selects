from django.contrib import admin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from .models import TestUser

@admin.register(TestUser)
class TestUserAdmin(AjaxSelectAdmin):
    form = make_ajax_form(TestUser)