import string

BASE62 = string.digits + string.ascii_letters  # 0-9 + a-z + A-Z
BASE = 62

def encode(num):
    s = []
    while num > 0:
        s.append(BASE62[num % BASE])
        num //= BASE
    return ''.join(reversed(s)) or '0'

def decode(s):
    num = 0
    for c in s:
        num = num * BASE + BASE62.index(c)
    return num


class URLShortener:
    def __init__(self):
        self.id = 0  # Simulate auto-increment ID
        self.url_map = {}         # id → long URL
        self.code_map = {}        # short code → id

    def shorten(self, long_url):
        self.id += 1
        self.url_map[self.id] = long_url
        code = encode(self.id)
        self.code_map[code] = self.id
        return f"https://sho.rt/{code}"

    def redirect(self, short_url):
        code = short_url.split("/")[-1]
        id = self.code_map.get(code)
        if id:
            return self.url_map[id]
        return None


s = URLShortener()

short = s.shorten("https://openai.com/chat")
print("Short URL:", short)

original = s.redirect(short)
print("Original URL:", original)
