# 📌 Purpose
# The Flyweight Pattern is used to minimize memory usage by sharing common, reusable objects (called flyweights) instead of creating new ones each time.

# It's especially useful when dealing with a large number of similar objects — like characters in a document, map tiles in a game, or icons in a file explorer.


# 📌 Purpose
# The Flyweight Pattern is used to minimize memory usage by sharing common, reusable objects (called flyweights) instead of creating new ones each time.

# It's especially useful when dealing with a large number of similar objects — like characters in a document, map tiles in a game, or icons in a file explorer.

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name              # Intrinsic (shared)
        self.color = color            # Intrinsic (shared)
        self.texture = texture        # Intrinsic (shared)

    def draw(self, x, y):
        print(f"Drawing {self.name} tree at ({x},{y}) with color {self.color} and texture '{self.texture}'")

class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory._tree_types:
            print(f"[Factory] Creating new TreeType: {key}")
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeFactory._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type: TreeType):
        self.x = x                    # Extrinsic (unique to each object)
        self.y = y
        self.tree_type = tree_type    # Shared flyweight

    def draw(self):
        self.tree_type.draw(self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()

if __name__ == "__main__":
    import random

    forest = Forest()
    
    tree_types = [
        ("Oak", "Green", "Rough"),
        ("Pine", "DarkGreen", "Pointy"),
        ("Cherry", "Pink", "Smooth")
    ]

    for _ in range(10):  # Simulate planting 10,000+ trees
        name, color, texture = random.choice(tree_types)
        x, y = random.randint(0, 100), random.randint(0, 100)
        forest.plant_tree(x, y, name, color, texture)

    print("\nRendering Forest:")
    forest.draw()


# 🧠 When to Use Flyweight Pattern
# Rendering engines (games, GUIs)

# Large documents (thousands of similar symbols)

# Caching and pooling (like database connections)

# Map tiles / icons (e.g., file explorers)