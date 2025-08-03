# ParkingLot
#  └── Floor(s)
#       └── Spot(s)
# Vehicle
#  └── Car, Bike, Bus
# Ticket



from datetime import datetime
import uuid

# --- Vehicle and Types ---
class VehicleType:
    CAR = "CAR"
    BIKE = "BIKE"
    BUS = "BUS"

class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

# --- Spot and Types ---
class SpotType:
    CAR = "CAR"
    BIKE = "BIKE"
    BUS = "BUS"

class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle = None

    def park(self, vehicle):
        self.vehicle = vehicle
        self.is_occupied = True

    def leave(self):
        self.vehicle = None
        self.is_occupied = False

# --- Ticket ---
class Ticket:
    def __init__(self, vehicle, spot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()

# --- Floor ---
class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def find_free_spot(self, vehicle_type):
        for spot in self.spots:
            if not spot.is_occupied and spot.spot_type == vehicle_type:
                return spot
        return None

# --- Parking Lot ---
class ParkingLot:
    def __init__(self):
        self.floors = []
        self.active_tickets = {}

    def add_floor(self, floor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spot = floor.find_free_spot(vehicle.vehicle_type)
            if spot:
                spot.park(vehicle)
                ticket = Ticket(vehicle, spot)
                self.active_tickets[ticket.ticket_id] = ticket
                print(f"Vehicle {vehicle.vehicle_number} parked at spot {spot.spot_id} on floor {floor.floor_number}")
                return ticket
        print("Parking Full!")
        return None

    def unpark_vehicle(self, ticket_id):
        ticket = self.active_tickets.get(ticket_id)
        if ticket:
            ticket.spot.leave()
            duration = (datetime.now() - ticket.entry_time).seconds
            print(f"Vehicle {ticket.vehicle.vehicle_number} unparked. Duration: {duration} seconds")
            del self.active_tickets[ticket_id]
        else:
            print("Invalid ticket")

# --- Example Usage ---
if __name__ == "__main__":
    lot = ParkingLot()

    # Create 1 floor with 3 spots
    floor1 = ParkingFloor(1)
    floor2 = ParkingFloor(2)
    floor1.add_spot(ParkingSpot("1A", SpotType.CAR))
    floor1.add_spot(ParkingSpot("1B", SpotType.BIKE))
    floor1.add_spot(ParkingSpot("1C", SpotType.CAR))
    floor2.add_spot(ParkingSpot("2A", SpotType.BIKE))


    lot.add_floor(floor1)
    lot.add_floor(floor2)
    # Vehicles
    car1 = Vehicle("GJ01AB1234", VehicleType.CAR)
    bike1 = Vehicle("GJ01CD5678", VehicleType.BIKE)
    bike2 = Vehicle("GJ01CD5679", VehicleType.BIKE)
    bike3 = Vehicle("GJ01CD5681", VehicleType.BIKE)

    # Park
    t1 = lot.park_vehicle(car1)
    t2 = lot.park_vehicle(bike1)
    t3 = lot.park_vehicle(bike2)
    t4 = lot.park_vehicle(bike3)
    print("Ticket ID:", t1.ticket_id)
    print("Vehicle Number:", t1.vehicle.vehicle_number)
    print("Spot ID:", t1.spot.spot_id)
    print("Entry Time:", t1.entry_time)
    # Unpark
    lot.unpark_vehicle(t1.ticket_id)
