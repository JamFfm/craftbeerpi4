import logging
import os
import sys


__all__ = ["CBPiExtension"]


logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class CBPiExtension():

    def init(self):
        pass

    def stop(self):
        pass

    def __init__(self, *args, **kwds):

        for a in kwds:

            super(CBPiExtension, self).__setattr__(a, kwds.get(a))
        self.cbpi = kwds.get("cbpi")
        self.id = kwds.get("id")
        self.value = None
        self.__dirty = False

    def __setattr__(self, name, value):

        if name != "_CBPiExtension__dirty":
            self.__dirty = True
            super(CBPiExtension, self).__setattr__(name, value)
        else:
            super(CBPiExtension, self).__setattr__(name, value)

    def load_config(self):
        from core.utils.utils import load_config as load
        path = os.path.dirname(sys.modules[self.__class__.__module__].__file__)
        try:
            return load("%s/config.yaml" % path)
        except:
            logger.warning("Faild to load config %s/config.yaml" % path)
