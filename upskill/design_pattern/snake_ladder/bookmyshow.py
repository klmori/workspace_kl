import uuid
import time
from collections import defaultdict

class User:
    def __init__(self, name):
        self.user_id = str(uuid.uuid4())
        self.name = name

class Movie:
    def __init__(self, name):
        self.movie_id = str(uuid.uuid4())
        self.name = name

class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id

class Show:
    def __init__(self, movie, screen, start_time):
        self.show_id = str(uuid.uuid4())
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.seats = [Seat(f"S{i}") for i in range(1, 11)]  # 10 seats

class Screen:
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.shows = []

class Theatre:
    def __init__(self, name):
        self.name = name
        self.screens = []

# --- Seat Locking Logic ---
class SeatLockProvider:
    def __init__(self, timeout=300):
        self.locked_seats = defaultdict(dict)  # show_id -> {seat_id: (user_id, lock_time)}
        self.timeout = timeout

    def lock_seat(self, show_id, seat_id, user_id):
        current_time = time.time()
        if self.is_seat_locked(show_id, seat_id):
            raise Exception(f"Seat {seat_id} is already locked.")
        self.locked_seats[show_id][seat_id] = (user_id, current_time)

    def unlock_expired_seats(self):
        now = time.time()
        for show_id in self.locked_seats:
            for seat in list(self.locked_seats[show_id]):
                _, lock_time = self.locked_seats[show_id][seat]
                if now - lock_time > self.timeout:
                    del self.locked_seats[show_id][seat]

    def is_seat_locked(self, show_id, seat_id):
        self.unlock_expired_seats()
        return seat_id in self.locked_seats[show_id]

# --- Booking Logic ---
class BookingService:
    def __init__(self, seat_locker):
        self.bookings = []  # list of (show_id, user_id, seats)
        self.seat_locker = seat_locker

    def book_seats(self, user, show, seat_ids):
        for seat_id in seat_ids:
            if self.seat_locker.is_seat_locked(show.show_id, seat_id):
                raise Exception(f"Seat {seat_id} is already locked.")

        # Lock all seats
        for seat_id in seat_ids:
            self.seat_locker.lock_seat(show.show_id, seat_id, user.user_id)

        # Simulate payment...
        time.sleep(1)  # mock delay

        # Confirm booking
        self.bookings.append((show.show_id, user.user_id, seat_ids))
        print(f"Booking confirmed for user {user.name}: {seat_ids}")



# Setup
movie = Movie("Oppenheimer")
theatre = Theatre("PVR")
screen = Screen("Screen 1")
show = Show(movie, screen, "8:00 PM")
screen.shows.append(show)
theatre.screens.append(screen)

# Users
user1 = User("Alice")
user2 = User("Bob")

# Services
seat_locker = SeatLockProvider(timeout=10)  # 10 sec lock
booking_service = BookingService(seat_locker)

# Booking
booking_service.book_seats(user1, show, ["S1", "S2"])  # ✅
# booking_service.book_seats(user2, show, ["S2", "S3"])  # ❌ Seat S2 already locked
