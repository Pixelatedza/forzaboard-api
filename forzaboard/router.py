from importlib import import_module
from rest_framework import routers


class Router(routers.DefaultRouter):

    def include(self, module_path):
        module = import_module(module_path)
        router = getattr(module, 'router', module)
        self.registry.extend(router.registry)
