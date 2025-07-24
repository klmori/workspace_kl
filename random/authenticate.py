import secrets
import time
from functools import wraps

# 1. Strategy Interface
class TokenStrategy:
    def generate_token(self, username):
        raise NotImplementedError
    
    def validate_token(self, token):
        raise NotImplementedError

    def invalidate_token(self, token):
        raise NotImplementedError

# 2. Concrete Strategy: Simple In-Memory Token Handling
class InMemoryTokenStrategy(TokenStrategy):
    def __init__(self, expiry_seconds=3600):
        self.tokens = {}  # token -> (username, expiry)
        self.expiry_seconds = expiry_seconds

    def generate_token(self, username):
        token = secrets.token_hex(16)
        expiry = time.time() + self.expiry_seconds
        self.tokens[token] = (username, expiry)
        return token

    def validate_token(self, token):
        if token not in self.tokens:
            return False, "Invalid token."
        username, expiry = self.tokens[token]
        if time.time() > expiry:
            del self.tokens[token]
            return False, "Token expired."
        return True, username

    def invalidate_token(self, token):
        if token in self.tokens:
            del self.tokens[token]
            return True
        return False

# 3. AuthManager uses a TokenStrategy
class AuthManager:
    def __init__(self, token_strategy: TokenStrategy):
        self.users = {}  # username -> password
        self.token_strategy = token_strategy

    def register(self, username, password):
        if username in self.users:
            return False, "User already exists."
        self.users[username] = password
        return True, "User registered successfully."

    def login(self, username, password):
        if self.users.get(username) == password:
            token = self.token_strategy.generate_token(username)
            return True, token
        return False, "Invalid username or password."

    def validate_token(self, token):
        return self.token_strategy.validate_token(token)

    def logout(self, token):
        success = self.token_strategy.invalidate_token(token)
        if success:
            return True, "Logged out."
        else:
            return False, "Invalid token."

    def require_token(self, func):
        @wraps(func)
        def wrapper(token, *args, **kwargs):
            valid, result = self.validate_token(token)
            if not valid:
                return False, f"Access denied: {result}"
            return func(result, *args, **kwargs)
        return wrapper

# Usage
token_strategy = InMemoryTokenStrategy(expiry_seconds=5)  # tokens expire after 5 seconds
auth = AuthManager(token_strategy)

@auth.require_token
def view_dashboard(username):
    return True, f"Welcome to your dashboard, {username}!"

# Register and login
auth.register("alice", "password123")
success, token_or_msg = auth.login("alice", "password123")

if success:
    print(view_dashboard(token_or_msg))  # Should succeed
    time.sleep(6)
    print(view_dashboard(token_or_msg))  # Should fail (token expired)
