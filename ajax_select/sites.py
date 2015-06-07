from ajax_select import LookupChannel

class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class AjaxSelectSite(object):

    def __init__(self):
        self._registry = {}

    def register(self, channel_or_iterable, lookup_class=None):

        if isinstance(channel_or_iterable, LookupChannel):
            channel_or_iterable = [channel_or_iterable]

        for channel in channel_or_iterable:
            if self.is_registered(channel):
                raise AlreadyRegistered('The channel %s is already registered' % channel.__name__)

        # Instantiate the lookup class to save in the registry
        self._registry[channel] = lookup_class(channel, self)

    def unregister(self, channel_or_iterable):
        """
        Unregisters the given model(s).
        If a model isn't already registered, this will raise NotRegistered.
        """
        if isinstance(channel_or_iterable, LookupChannel):
            channel_or_iterable = [channel_or_iterable]
        for channel in channel_or_iterable:
            if not self.is_registered(channel):
                raise NotRegistered('The channel %s is not registered' % channel.__name__)
            del self._registry[channel]


    def is_registered(self, model):
        """
        Check if a model class is registered with this `AjaxSelectSite`.
        """
        return model in self._registry


site = AjaxSelectSite()