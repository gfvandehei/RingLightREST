from dependency_injector import providers, containers
from RingLightAPI.services.devicefinder import LightDeviceFinder


class BaseContainer(containers.DeclarativeContainer):
    light_finder = providers.Singleton(LightDeviceFinder, light_factory=None)


def start_container(self):
    BaseContainer.light_finder().start()