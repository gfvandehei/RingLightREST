from RingLightAPI.containers.basecontainer import BaseContainer
from RingLightAPI import create_app

if __name__ == "__main__":
    
    BaseContainer.config.from_yaml('config.yaml')

    listener = BaseContainer.light_finder()
    listener.start()

    create_app()