from enum import Enum
from collections import deque

# --- Enums ---
class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3

class ElevatorState(Enum):
    MOVING = 1
    STOPPED = 2
    IDLE = 3

# --- Request ---
class Request:
    def __init__(self, floor, direction=None):
        self.floor = floor
        self.direction = direction

# --- Elevator ---
class Elevator:
    def __init__(self, eid):
        self.id = eid
        self.current_floor = 0
        self.direction = Direction.IDLE
        self.state = ElevatorState.IDLE
        self.requests = deque()

    def add_request(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)

    def move(self):
        if not self.requests:
            self.state = ElevatorState.IDLE
            self.direction = Direction.IDLE
            return

        next_floor = self.requests[0]
        if self.current_floor < next_floor:
            self.current_floor += 1
            self.direction = Direction.UP
        elif self.current_floor > next_floor:
            self.current_floor -= 1
            self.direction = Direction.DOWN
        else:
            print(f"Elevator {self.id} stopped at floor {self.current_floor}")
            self.requests.popleft()
            self.state = ElevatorState.STOPPED
            if not self.requests:
                self.state = ElevatorState.IDLE
                self.direction = Direction.IDLE

    def status(self):
        return f"Elevator {self.id}: Floor {self.current_floor} | {self.direction.name} | Requests: {list(self.requests)}"

# --- Elevator System ---
class ElevatorSystem:
    def __init__(self, num_elevators=1):
        self.elevators = [Elevator(i) for i in range(num_elevators)]

    def request_elevator(self, floor, direction):
        best = self.find_best_elevator(floor, direction)
        if best is not None:
            best.add_request(floor)
        else:
            print("No elevator available right now.")

    def find_best_elevator(self, floor, direction):
        # Simple: return first idle or nearest moving elevator
        for elevator in self.elevators:
            if elevator.state == ElevatorState.IDLE:
                return elevator
        return self.elevators[0]  # fallback

    def step(self):
        for elevator in self.elevators:
            elevator.move()

    def status(self):
        for e in self.elevators:
            print(e.status())

# --- Example ---
if __name__ == "__main__":
    system = ElevatorSystem(2)
    system.request_elevator(3, Direction.UP)
    system.request_elevator(5, Direction.DOWN)

    for _ in range(10):
        system.step()
        system.status()
        print("---")
