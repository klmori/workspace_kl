# Notify many objects of a change	
# Email/SMS notification


class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, obs):
        self._observers.append(obs)

    def notify(self):
        for obs in self._observers:
            obs.update(self._temperature)

    def set_temperature(self, temp):
        self._temperature = temp
        self.notify()

class DisplayUnit:
    def update(self, temperature):
        print(f"Display: Temperature updated to {temperature}°C")

class Logger:
    def update(self, temperature):
        print(f"Logger: Logged temperature = {temperature}°C")

# Usage
station = WeatherStation()
station.register_observer(DisplayUnit())
station.register_observer(Logger())

station.set_temperature(25)
station.set_temperature(30)
