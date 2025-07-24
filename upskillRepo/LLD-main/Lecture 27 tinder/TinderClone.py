import math
import time
from datetime import datetime
from enum import Enum
from typing import List, Dict

# -------------------- Observer Pattern -------------------- #
class NotificationObserver:
    def update(self, message: str):
        raise NotImplementedError

class UserNotificationObserver(NotificationObserver):
    def __init__(self, user_id: str):
        self.user_id = user_id
    def update(self, message: str):
        print(f"Notification for user {self.user_id}: {message}")

class NotificationService:
    _instance = None
    def __init__(self):
        self.observers: Dict[str, NotificationObserver] = {}
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = NotificationService()
        return cls._instance
    def register_observer(self, user_id: str, observer: NotificationObserver):
        self.observers[user_id] = observer
    def remove_observer(self, user_id: str):
        self.observers.pop(user_id, None)
    def notify_user(self, user_id: str, message: str):
        if user_id in self.observers:
            self.observers[user_id].update(message)
    def notify_all(self, message: str):
        for observer in self.observers.values():
            observer.update(message)

# -------------------- Basic Models -------------------- #
class Gender(Enum):
    MALE = 1
    FEMALE = 2
    NON_BINARY = 3
    OTHER = 4

class Location:
    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = latitude
        self.longitude = longitude
    def set_latitude(self, lat):
        self.latitude = lat
    def set_longitude(self, lon):
        self.longitude = lon
    def get_latitude(self):
        return self.latitude
    def get_longitude(self):
        return self.longitude
    def distance_in_km(self, other):
        earth_radius_km = 6371.0
        dlat = math.radians(other.latitude - self.latitude)
        dlon = math.radians(other.longitude - self.longitude)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(self.latitude)) * math.cos(math.radians(other.latitude)) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return earth_radius_km * c

class Interest:
    def __init__(self, name="", category=""):
        self.name = name
        self.category = category
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category

class Preference:
    def __init__(self):
        self.interested_in: List[Gender] = []
        self.min_age = 18
        self.max_age = 100
        self.max_distance = 100.0
        self.interests: List[str] = []
    def add_gender_preference(self, gender: Gender):
        self.interested_in.append(gender)
    def remove_gender_preference(self, gender: Gender):
        if gender in self.interested_in:
            self.interested_in.remove(gender)
    def set_age_range(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age
    def set_max_distance(self, distance):
        self.max_distance = distance
    def add_interest(self, interest):
        self.interests.append(interest)
    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)
    def is_interested_in_gender(self, gender):
        return gender in self.interested_in
    def is_age_in_range(self, age):
        return self.min_age <= age <= self.max_age
    def is_distance_acceptable(self, distance):
        return distance <= self.max_distance
    def get_interests(self):
        return self.interests
    def get_interested_genders(self):
        return self.interested_in
    def get_min_age(self):
        return self.min_age
    def get_max_age(self):
        return self.max_age
    def get_max_distance(self):
        return self.max_distance

# -------------------- Message System -------------------- #
class Message:
    def __init__(self, sender_id, content):
        self.sender_id = sender_id
        self.content = content
        self.timestamp = int(time.time() * 1000)
    def get_sender_id(self):
        return self.sender_id
    def get_content(self):
        return self.content
    def get_timestamp(self):
        return self.timestamp
    def get_formatted_time(self):
        return datetime.fromtimestamp(self.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')

class ChatRoom:
    def __init__(self, room_id, user1_id, user2_id):
        self.id = room_id
        self.participant_ids = [user1_id, user2_id]
        self.messages: List[Message] = []
    def get_id(self):
        return self.id
    def add_message(self, sender_id, content):
        msg = Message(sender_id, content)
        self.messages.append(msg)
    def has_participant(self, user_id):
        return user_id in self.participant_ids
    def get_messages(self):
        return self.messages
    def get_participants(self):
        return self.participant_ids
    def display_chat(self):
        print(f"===== Chat Room: {self.id} =====")
        for msg in self.messages:
            print(f"[{msg.get_formatted_time()}] {msg.get_sender_id()}: {msg.get_content()}")
        print("=========================")

# -------------------- Profile System -------------------- #
class UserProfile:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = Gender.OTHER
        self.bio = ""
        self.photos: List[str] = []
        self.interests: List[Interest] = []
        self.location = Location()
    def set_name(self, n):
        self.name = n
    def set_age(self, a):
        self.age = a
    def set_gender(self, g):
        self.gender = g
    def set_bio(self, b):
        self.bio = b
    def add_photo(self, photo_url):
        self.photos.append(photo_url)
    def remove_photo(self, photo_url):
        if photo_url in self.photos:
            self.photos.remove(photo_url)
    def add_interest(self, name, category):
        self.interests.append(Interest(name, category))
    def remove_interest(self, name):
        self.interests = [i for i in self.interests if i.get_name() != name]
    def set_location(self, loc):
        self.location = loc
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_bio(self):
        return self.bio
    def get_photos(self):
        return self.photos
    def get_interests(self):
        return self.interests
    def get_location(self):
        return self.location
    def display(self):
        print("===== Profile =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender.name.capitalize()}")
        print(f"Bio: {self.bio}")
        print(f"Photos: {', '.join(self.photos)}")
        print("Interests: ", end="")
        for i in self.interests:
            print(f"{i.get_name()} ({i.get_category()}), ", end="")
        print()
        print(f"Location: {self.location.get_latitude()}, {self.location.get_longitude()}")
        print("===================")

# -------------------- User System -------------------- #
class SwipeAction(Enum):
    LEFT = 1
    RIGHT = 2

class User:
    def __init__(self, user_id):
        self.id = user_id
        self.profile = UserProfile()
        self.preference = Preference()
        self.swipe_history: Dict[str, SwipeAction] = {}
        self.notification_observer = UserNotificationObserver(user_id)
        NotificationService.get_instance().register_observer(user_id, self.notification_observer)
    def get_id(self):
        return self.id
    def get_profile(self):
        return self.profile
    def get_preference(self):
        return self.preference
    def swipe(self, other_user_id, action: SwipeAction):
        self.swipe_history[other_user_id] = action
    def has_liked(self, other_user_id):
        return self.swipe_history.get(other_user_id) == SwipeAction.RIGHT
    def has_disliked(self, other_user_id):
        return self.swipe_history.get(other_user_id) == SwipeAction.LEFT
    def has_interacted_with(self, other_user_id):
        return other_user_id in self.swipe_history
    def display_profile(self):
        self.profile.display()

# -------------------- Location Service -------------------- #
class LocationStrategy:
    def find_nearby_users(self, location: Location, max_distance: float, all_users: List[User]) -> List[User]:
        raise NotImplementedError

class BasicLocationStrategy(LocationStrategy):
    def find_nearby_users(self, location: Location, max_distance: float, all_users: List[User]) -> List[User]:
        nearby_users = []
        for user in all_users:
            distance = location.distance_in_km(user.get_profile().get_location())
            if distance <= max_distance:
                nearby_users.append(user)
        return nearby_users

class LocationService:
    _instance = None
    def __init__(self):
        self.strategy = BasicLocationStrategy()
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = LocationService()
        return cls._instance
    def set_strategy(self, new_strategy: LocationStrategy):
        self.strategy = new_strategy
    def find_nearby_users(self, location: Location, max_distance: float, all_users: List[User]) -> List[User]:
        return self.strategy.find_nearby_users(location, max_distance, all_users)

# -------------------- Matching System -------------------- #
class MatcherType(Enum):
    BASIC = 1
    INTERESTS_BASED = 2
    LOCATION_BASED = 3

class Matcher:
    def calculate_match_score(self, user1: User, user2: User) -> float:
        raise NotImplementedError

class BasicMatcher(Matcher):
    def calculate_match_score(self, user1: User, user2: User) -> float:
        user1_likes_user2_gender = user1.get_preference().is_interested_in_gender(user2.get_profile().get_gender())
        user2_likes_user1_gender = user2.get_preference().is_interested_in_gender(user1.get_profile().get_gender())
        if not user1_likes_user2_gender or not user2_likes_user1_gender:
            return 0.0
        user1_likes_user2_age = user1.get_preference().is_age_in_range(user2.get_profile().get_age())
        user2_likes_user1_age = user2.get_preference().is_age_in_range(user1.get_profile().get_age())
        if not user1_likes_user2_age or not user2_likes_user1_age:
            return 0.0
        distance = user1.get_profile().get_location().distance_in_km(user2.get_profile().get_location())
        user1_likes_user2_distance = user1.get_preference().is_distance_acceptable(distance)
        user2_likes_user1_distance = user2.get_preference().is_distance_acceptable(distance)
        if not user1_likes_user2_distance or not user2_likes_user1_distance:
            return 0.0
        return 0.5

class InterestsBasedMatcher(Matcher):
    def calculate_match_score(self, user1: User, user2: User) -> float:
        base_score = BasicMatcher().calculate_match_score(user1, user2)
        if base_score == 0.0:
            return 0.0
        user1_interest_names = [i.get_name() for i in user1.get_profile().get_interests()]
        shared_interests = 0
        for interest in user2.get_profile().get_interests():
            if interest.get_name() in user1_interest_names:
                shared_interests += 1
        max_interests = max(len(user1.get_profile().get_interests()), len(user2.get_profile().get_interests()))
        interest_score = 0.5 * (shared_interests / max_interests) if max_interests > 0 else 0.0
        return base_score + interest_score

class LocationBasedMatcher(Matcher):
    def calculate_match_score(self, user1: User, user2: User) -> float:
        base_score = InterestsBasedMatcher().calculate_match_score(user1, user2)
        if base_score == 0.0:
            return 0.0
        distance = user1.get_profile().get_location().distance_in_km(user2.get_profile().get_location())
        max_distance = min(user1.get_preference().get_max_distance(), user2.get_preference().get_max_distance())
        proximity_score = 0.2 * (1.0 - (distance / max_distance)) if max_distance > 0 else 0.0
        return base_score + proximity_score

class MatcherFactory:
    @staticmethod
    def create_matcher(type_: MatcherType) -> Matcher:
        if type_ == MatcherType.BASIC:
            return BasicMatcher()
        elif type_ == MatcherType.INTERESTS_BASED:
            return InterestsBasedMatcher()
        elif type_ == MatcherType.LOCATION_BASED:
            return LocationBasedMatcher()
        else:
            return BasicMatcher()

# -------------------- Dating App -------------------- #
class DatingApp:
    _instance = None
    def __init__(self):
        self.users: List[User] = []
        self.chat_rooms: List[ChatRoom] = []
        self.matcher: Matcher = MatcherFactory.create_matcher(MatcherType.LOCATION_BASED)
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatingApp()
        return cls._instance
    def set_matcher(self, type_: MatcherType):
        self.matcher = MatcherFactory.create_matcher(type_)
    def create_user(self, user_id: str) -> User:
        user = User(user_id)
        self.users.append(user)
        return user
    def get_user_by_id(self, user_id: str) -> User:
        for user in self.users:
            if user.get_id() == user_id:
                return user
        return None
    def find_nearby_users(self, user_id: str, max_distance: float) -> List[User]:
        user = self.get_user_by_id(user_id)
        if user is None:
            return []
        nearby_users = LocationService.get_instance().find_nearby_users(user.get_profile().get_location(), max_distance, self.users)
        nearby_users = [u for u in nearby_users if u.get_id() != user_id]
        filtered_users = []
        for other_user in nearby_users:
            if not user.has_interacted_with(other_user.get_id()):
                score = self.matcher.calculate_match_score(user, other_user)
                if score > 0:
                    filtered_users.append(other_user)
        return filtered_users
    def swipe(self, user_id: str, target_user_id: str, action: SwipeAction):
        user = self.get_user_by_id(user_id)
        target_user = self.get_user_by_id(target_user_id)
        if user is None or target_user is None:
            print("User not found.")
            return False
        user.swipe(target_user_id, action)
        if action == SwipeAction.RIGHT and target_user.has_liked(user_id):
            chat_room_id = f"{user_id}_{target_user_id}"
            chat_room = ChatRoom(chat_room_id, user_id, target_user_id)
            self.chat_rooms.append(chat_room)
            NotificationService.get_instance().notify_user(user_id, f"You have a new match with {target_user.get_profile().get_name()}!")
            NotificationService.get_instance().notify_user(target_user_id, f"You have a new match with {user.get_profile().get_name()}!")
            return True
        return False
    def get_chat_room(self, user1_id: str, user2_id: str):
        for chat_room in self.chat_rooms:
            if chat_room.has_participant(user1_id) and chat_room.has_participant(user2_id):
                return chat_room
        return None
    def send_message(self, sender_id: str, receiver_id: str, content: str):
        chat_room = self.get_chat_room(sender_id, receiver_id)
        if chat_room is None:
            print("No chat room found between these users.")
            return
        chat_room.add_message(sender_id, content)
        NotificationService.get_instance().notify_user(receiver_id, f"New message from {self.get_user_by_id(sender_id).get_profile().get_name()}")
    def display_user(self, user_id: str):
        user = self.get_user_by_id(user_id)
        if user is None:
            print("User not found.")
            return
        user.display_profile()
    def display_chat_room(self, user1_id: str, user2_id: str):
        chat_room = self.get_chat_room(user1_id, user2_id)
        if chat_room is None:
            print("No chat room found between these users.")
            return
        chat_room.display_chat()

# -------------------- Main -------------------- #
if __name__ == "__main__":
    app = DatingApp.get_instance()
    user1 = app.create_user("user1")
    user2 = app.create_user("user2")
    profile1 = user1.get_profile()
    profile1.set_name("Rohan")
    profile1.set_age(28)
    profile1.set_gender(Gender.MALE)
    profile1.set_bio("I am a software developer")
    profile1.add_photo("rohan_photo1.jpg")
    profile1.add_interest("Coding", "Programming")
    profile1.add_interest("Travel", "Lifestyle")
    profile1.add_interest("Music", "Entertainment")
    pref1 = user1.get_preference()
    pref1.add_gender_preference(Gender.FEMALE)
    pref1.set_age_range(25, 30)
    pref1.set_max_distance(10.0)
    pref1.add_interest("Coding")
    pref1.add_interest("Travel")
    profile2 = user2.get_profile()
    profile2.set_name("Neha")
    profile2.set_age(27)
    profile2.set_gender(Gender.FEMALE)
    profile2.set_bio("Art teacher who loves painting and traveling.")
    profile2.add_photo("neha_photo1.jpg")
    profile2.add_interest("Painting", "Art")
    profile2.add_interest("Travel", "Lifestyle")
    profile2.add_interest("Music", "Entertainment")
    pref2 = user2.get_preference()
    pref2.add_gender_preference(Gender.MALE)
    pref2.set_age_range(27, 30)
    pref2.set_max_distance(15.0)
    pref2.add_interest("Coding")
    pref2.add_interest("Movies")
    location1 = Location()
    location1.set_latitude(1.01)
    location1.set_longitude(1.02)
    profile1.set_location(location1)
    location2 = Location()
    location2.set_latitude(1.03)
    location2.set_longitude(1.04)
    profile2.set_location(location2)
    print("---- User Profiles ----")
    app.display_user("user1")
    app.display_user("user2")
    print("\n---- Nearby Users for user1 (within 5km) ----")
    nearby_users = app.find_nearby_users("user1", 5.0)
    print(f"Found {len(nearby_users)} nearby users")
    for user in nearby_users:
        print(f"- {user.get_profile().get_name()} ({user.get_id()})")
    print("\n---- Swipe Actions ----")
    print("User1 swipes right on User2")
    app.swipe("user1", "user2", SwipeAction.RIGHT)
    print("User2 swipes right on User1")
    app.swipe("user2", "user1", SwipeAction.RIGHT)
    print("\n---- Chat Room ----")
    app.send_message("user1", "user2", "Hi Neha, Kaise ho?")
    app.send_message("user2", "user1", "Hi Rohan, Ma bdiya tum btao")
    app.display_chat_room("user1", "user2")
