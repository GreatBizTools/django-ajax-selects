from django.utils.html import escape
from ajax_select import LookupChannel

from .models import TestUser


class TestUserLookup(LookupChannel):
    model = TestUser

    def get_query(self, q, request):
        return TestUser.objects.find_active_by_name_or_company(q)

    def format_match(self, obj):
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        return u"%s - %s" % (escape(obj.company), escape(obj), )
