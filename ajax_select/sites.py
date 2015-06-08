from ajax_select import LookupChannel

class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class AjaxSelectSite(object):

    def __init__(self):
        self._registry = {}

    def register(self, lookup_labels):

        # channel data structure is { 'channel' : ( module.lookup, lookupclass ) }
        # or                        { 'channel' : { 'model': 'xxxxx', 'search_field': 'xxxx' }
        merge_dict(self._registry, lookup_labels)

    def unregister(self, lookup_labels):
        """
        Unregisters the given model(s).
        If a model isn't already registered, this will raise NotRegistered.
        """
        # channel data structure is { label : ( module.lookup, lookupclass ) }
        for channel_name in lookup_labels.keys():
            if not self.is_registered(channel_name):
                raise NotRegistered('The channel %s is not registered' % channel_name)
            del self._registry[channel_name]

    def is_registered(self, label):
        """
        Check if a LookupChannel class is registered with this `AjaxSelectSite`.
        """
        return label in self._registry

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


class AutoDiscover():

    def __getitem__(self, key):
        if not hasattr(self, 'channels'):
            self.channels = self.discover_channels()
        return self.channels[key]

    @staticmethod
    def discover_channels():
        from django.conf import settings

        channels = {}

        for app in settings.INSTALLED_APPS:
            try:
                app_root = getattr(app)
                lookup = getattr(app_root, 'lookup')

                if hasattr(lookup, "AJAX_LOOKUP_CHANNELS"):
                    channels = merge_dict(channels, lookup.AJAX_LOOKUP_CHANNELS)
            except:
                pass

        return channels


site = AjaxSelectSite()