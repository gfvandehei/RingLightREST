from dependency_injector import providers, containers
from RingLightAPI.services.mqttclient import MqttClient
from RingLightAPI.services.mqttlighting import MQTTLightingController
from RingLightAPI.config import Configs

class Services(containers.DeclarativeContainer):
    mqtt_client = providers.Singleton(MqttClient, Configs.config)
    mqtt_lighting = providers.Singleton(MQTTLightingController, mqtt_client=mqtt_client)

def create_init():
    l = Services.mqtt_lighting()
    l.start()
