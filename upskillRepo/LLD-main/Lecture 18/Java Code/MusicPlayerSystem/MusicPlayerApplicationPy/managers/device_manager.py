
from enums.device_type import DeviceType
from factories.device_factory import DeviceFactory

class DeviceManager:
    _instance = None
    def __init__(self):
        self.current_output_device = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DeviceManager()
        return cls._instance
    def connect(self, device_type):
        self.current_output_device = DeviceFactory.create_device(device_type)
        if device_type == DeviceType.BLUETOOTH:
            print("Bluetooth device connected")
        elif device_type == DeviceType.WIRED:
            print("Wired device connected")
        elif device_type == DeviceType.HEADPHONES:
            print("Headphones connected")
    def get_output_device(self):
        if self.current_output_device is None:
            raise Exception("No output device is connected.")
        return self.current_output_device
    def has_output_device(self):
        return self.current_output_device is not None
