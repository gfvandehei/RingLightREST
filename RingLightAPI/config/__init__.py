from dependency_injector import providers, containers

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')