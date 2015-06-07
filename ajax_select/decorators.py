def register(*models, **kwargs):
    """
    Registers the given model(s) classes and wrapped ModelAdmin class with
    admin site:
    @register(Author)
    class AuthorAdmin(admin.ModelAdmin):
        pass
    A kwarg of `site` can be passed as the admin site, otherwise the default
    admin site will be used.
    """
    from ajax_select import LookupChannel
    from ajax_select.sites import site

    def _ajax_select_wrapper(lookup_class):

        if not issubclass(lookup_class, LookupChannel):
            raise ValueError('Wrapped class must subclass LookupChannel.')

        site.register(models, lookup_class=lookup_class)

        return lookup_class
    return _ajax_select_wrapper