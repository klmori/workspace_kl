from enum import Enum

class PlayStrategyType(Enum):
    SEQUENTIAL = 1
    RANDOM = 2
    CUSTOM_QUEUE = 3

class DeviceType(Enum):
    BLUETOOTH = 1
    WIRED = 2
    HEADPHONES = 3
