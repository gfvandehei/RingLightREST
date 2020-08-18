from dependency_injector import providers, containers
from RingLightAPI.services.devicefinder import LightDeviceFinder
from RingLightAPI.services.light_factory import LightFactory
from RingLightAPI.services.light_store import LightStore

class BaseContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    light_store = providers.Singleton(LightStore)
    light_factory = providers.Singleton(LightFactory, light_store = light_store)
    light_finder = providers.Singleton(LightDeviceFinder, config.listener.port, light_factory=light_factory)


def start_container():
    light_store = BaseContainer.light_store()
    light_fac = BaseContainer.light_factory()
    light_finder = BaseContainer.light_finder()

    light_finder.start()