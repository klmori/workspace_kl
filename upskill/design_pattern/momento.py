# ✅ Purpose
# The Memento Pattern is used to capture and restore an object’s internal state without violating encapsulation. It's helpful for implementing undo/redo, rollback, or history functionality.



# 🏪 Real-Life Analogy: Text Editor with Undo
# In a text editor like Notepad or Google Docs, you can hit "Undo" to go back to a previous state. Behind the scenes, the editor saves a snapshot of your document (a memento) before every change.

# Originator: The document/text editor that changes.

# Memento: A snapshot of the content at a given time.

# Caretaker: Manages saving and restoring mementos (Undo Manager).

# MEMENTO: Stores the state of the Editor
class EditorMemento:
    def __init__(self, content, cursor_position):
        self._content = content
        self._cursor_position = cursor_position

    def get_content(self):
        return self._content

    def get_cursor_position(self):
        return self._cursor_position


# ORIGINATOR: The editor that creates/restores mementos
class TextEditor:
    def __init__(self):
        self._content = ""
        self._cursor_position = 0

    def type_text(self, text):
        before = self._content[:self._cursor_position]
        after = self._content[self._cursor_position:]
        self._content = before + text + after
        self._cursor_position += len(text)

    def move_cursor(self, pos):
        self._cursor_position = max(0, min(pos, len(self._content)))

    def delete(self):
        if self._cursor_position > 0:
            self._content = self._content[:self._cursor_position - 1] + self._content[self._cursor_position:]
            self._cursor_position -= 1

    def save(self):
        return EditorMemento(self._content, self._cursor_position)

    def restore(self, memento):
        self._content = memento.get_content()
        self._cursor_position = memento.get_cursor_position()

    def display(self):
        cursor = " " * self._cursor_position + "^"
        print(f"[Editor] Content: '{self._content}'\n          Cursor:  {cursor}")


# CARETAKER: Maintains the history of editor states
class HistoryManager:
    def __init__(self):
        self._history = []

    def push(self, memento):
        self._history.append(memento)

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()


# CLIENT
if __name__ == "__main__":
    editor = TextEditor()
    history = HistoryManager()

    editor.type_text("Hello")
    history.push(editor.save())

    editor.type_text(", world")
    history.push(editor.save())

    editor.type_text("!!!")
    editor.display()

    print("\n🔁 Undoing...")
    editor.restore(history.undo())  # Undo !!!
    editor.display()

    print("\n🔁 Undoing again...")
    editor.restore(history.undo())  # Undo ", world"
    editor.display()



# 🛠️ Use Cases
# Use Case	Description
# Undo/Redo	Editors, drawing tools, IDEs
# Game State	Save checkpoints and load on failure
# Transactions	Restore previous valid state after failure
# Configuration	Revert to default or last saved settings


# 🏁 Summary
# Concept	Description
# Pattern Name	Memento
# Purpose	Save and restore object state without exposing it
# Real-World	Undo in text editors or checkpoints in games
# Key Parts	Originator, Memento, Caretaker