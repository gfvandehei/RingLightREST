from abc import ABC, abstractmethod, abstractproperty
import uuid


class LightSource(ABC):

    name: str
    address: str
    state: object
    uuid: int
    type_id: str = "base"

    def __init__(self, name:str, address: str):
        self.name = name
        self.address = address
        self.uuid = uuid.uuid4().int

    @abstractmethod
    def set_color(self, r, g, b, brightness):
        raise NotImplementedError("set_color not implemented")

