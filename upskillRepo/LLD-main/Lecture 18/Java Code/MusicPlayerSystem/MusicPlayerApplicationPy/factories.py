from enums import DeviceType
from device import BluetoothSpeakerAdapter, HeadphonesAdapter, WiredSpeakerAdapter
from external import BluetoothSpeakerAPI, HeadphonesAPI, WiredSpeakerAPI

def create_device(device_type):
    if device_type == DeviceType.BLUETOOTH:
        return BluetoothSpeakerAdapter(BluetoothSpeakerAPI())
    elif device_type == DeviceType.WIRED:
        return WiredSpeakerAdapter(WiredSpeakerAPI())
    elif device_type == DeviceType.HEADPHONES:
        return HeadphonesAdapter(HeadphonesAPI())
    else:
        return HeadphonesAdapter(HeadphonesAPI())

class DeviceFactory:
    @staticmethod
    def create_device(device_type):
        return create_device(device_type)
