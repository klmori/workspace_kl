# 🔍 Purpose
# The Bridge pattern is used to decouple an abstraction from its implementation so that the two can vary independently.

# It separates the interface (abstraction) from the actual implementation (platform-specific logic). This is helpful when both abstractions and implementations may evolve over time.



# 🧠 Real-Life Analogy: Remote Control & Devices
# Think of a remote control and the devices it controls:

# Remote control is the abstraction

# Devices (TV, Radio, etc.) are implementations

# The same remote interface can work with different devices, and new remotes or devices can be added without changing the existing code.

from abc import ABC, abstractmethod

# ----------------------------
# Implementation Hierarchy (Device Side)
# ----------------------------

class Device(ABC):
    @abstractmethod
    def turn_on(self): pass

    @abstractmethod
    def turn_off(self): pass

    @abstractmethod
    def set_channel(self, channel): pass


class TV(Device):
    def turn_on(self):
        print("Turning on the TV")

    def turn_off(self):
        print("Turning off the TV")

    def set_channel(self, channel):
        print(f"TV channel set to {channel}")


class Radio(Device):
    def turn_on(self):
        print("Turning on the Radio")

    def turn_off(self):
        print("Turning off the Radio")

    def set_channel(self, channel):
        print(f"Radio frequency set to {channel} MHz")


# ----------------------------
# Abstraction Hierarchy (Remote Side)
# ----------------------------

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_channel(self, channel):
        self.device.set_channel(channel)


# Extended abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Muting the device")


# ----------------------------
# Client
# ----------------------------

def main():
    tv = TV()
    radio = Radio()

    # Basic remote for TV
    basic_remote = RemoteControl(tv)
    basic_remote.turn_on()
    basic_remote.set_channel(5)
    basic_remote.turn_off()

    print("---")

    # Advanced remote for Radio
    adv_remote = AdvancedRemoteControl(radio)
    adv_remote.turn_on()
    adv_remote.set_channel(101.1)
    adv_remote.mute()
    adv_remote.turn_off()

if __name__ == "__main__":
    main()



# 🧰 Real-World Examples
# Domain	Abstraction	Implementation
# Remote Devices	Remote	TV, Radio, Projector
# UI Toolkits	UI Widget	Windows, macOS, Linux rendering
# Payment Systems	Payment UI	Stripe, Razorpay, PayPal
# Drawing Shapes	Shape (Circle)	Raster renderer, Vector renderer
# Messaging App	Chat App	SMS, WhatsApp, Slack integrations
