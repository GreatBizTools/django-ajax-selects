from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from ajax_select import LookupChannel

class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class AjaxSelectSite(object):

    def __init__(self):
        self._registry = {}

    def merge_dict(d1, d2):
        """
        Merges two dictionaries into one new dict using copy()
        :param d1: Dict()
        :param d2: Dict()
        :return: Dict()
        """
        merged = d1.copy()
        merged.update(d2)
        return merged

     def register(self, model_or_iterable, lookup_class=None):

        if isinstance(model_or_iterable, LookupChannel):
            model_or_iterable = [model_or_iterable]

        for model in model_or_iterable:
            if model in self._registry:
                raise AlreadyRegistered('The model %s is already registered' % model.__name__)

        # Instantiate the lookup class to save in the registry
        self._registry[model] = lookup_class(model, self)

    def unregister(self, model_or_iterable):
        """
        Unregisters the given model(s).
        If a model isn't already registered, this will raise NotRegistered.
        """
        if isinstance(model_or_iterable, LookupChannel):
            model_or_iterable = [model_or_iterable]
        for model in model_or_iterable:
            if model not in self._registry:
                raise NotRegistered('The model %s is not registered' % model.__name__)
            del self._registry[model]


    def is_registered(self, model):
        """
        Check if a model class is registered with this `AjaxSelectSite`.
        """
        return model in self._registry


site = AjaxSelectSite()