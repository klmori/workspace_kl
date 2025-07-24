

from enums.device_type import DeviceType
from device.bluetooth_speaker_adapter import BluetoothSpeakerAdapter
from device.headphones_adapter import HeadphonesAdapter
from device.wired_speaker_adapter import WiredSpeakerAdapter
from external.bluetooth_speaker_api import BluetoothSpeakerAPI
from external.headphones_api import HeadphonesAPI
from external.wired_speaker_api import WiredSpeakerAPI

class DeviceFactory:
    @staticmethod
    def create_device(device_type):
        if device_type == DeviceType.BLUETOOTH:
            return BluetoothSpeakerAdapter(BluetoothSpeakerAPI())
        elif device_type == DeviceType.WIRED:
            return WiredSpeakerAdapter(WiredSpeakerAPI())
        elif device_type == DeviceType.HEADPHONES:
            return HeadphonesAdapter(HeadphonesAPI())
        else:
            return HeadphonesAdapter(HeadphonesAPI())
