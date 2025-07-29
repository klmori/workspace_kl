# Provide a simplified interface to a complex system (multiple classes/subsystems).

# To order food, you don’t talk to the chef, cashier, and manager.
# → You just use the counter guy (the facade) to deal with everything.


# 💼 Scenario:
# You want to book a flight, which involves:

# Searching flights

# Booking a seat

# Sending confirmation

# Logging

# You want clients to use 1 method, not 4 systems.


# Subsystems
class FlightSearchSystem:
    def search(self, src, dest):
        print(f"Searching flights from {src} to {dest}")
        return "Flight123"

class SeatBookingSystem:
    def book(self, flight_id):
        print(f"Booking seat on {flight_id}")
        return "Seat42A"

class NotificationSystem:
    def notify(self, seat):
        print(f"Notification: Seat {seat} booked successfully!")

class LoggingSystem:
    def log(self, msg):
        print(f"[LOG]: {msg}")

# Facade
class FlightBookingFacade:
    def __init__(self):
        self.search_system = FlightSearchSystem()
        self.booking_system = SeatBookingSystem()
        self.notification_system = NotificationSystem()
        self.logger = LoggingSystem()

    def book_flight(self, src, dest):
        flight = self.search_system.search(src, dest)
        seat = self.booking_system.book(flight)
        self.notification_system.notify(seat)
        self.logger.log(f"Booked {seat} on {flight} from {src} to {dest}")

# Client
facade = FlightBookingFacade()
facade.book_flight("Delhi", "Mumbai")
