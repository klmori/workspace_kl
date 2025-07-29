# 🧠 Use Cases
# Undo/redo systems (like editors)

# Task queues

# Transaction management

# Game controls

# 💼 Scenario:
# You're building a home automation system with:

# Lights

# AC

# Music

# You want to:

# Queue commands

# Undo commands

# Receiver
class Light:
    def on(self): print("💡 Light ON")
    def off(self): print("💡 Light OFF")

class AC:
    def start(self): print("❄️ AC STARTED")
    def stop(self): print("❄️ AC STOPPED")

# Command interface
class Command:
    def execute(self): pass
    def undo(self): pass

# Concrete commands
class LightOnCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.on()
    def undo(self): self.light.off()

class ACStartCommand(Command):
    def __init__(self, ac): self.ac = ac
    def execute(self): self.ac.start()
    def undo(self): self.ac.stop()

# Invoker
class RemoteControl:
    def __init__(self): self.history = []

    def press(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()

# Client
light = Light()
ac = AC()

light_cmd = LightOnCommand(light)
ac_cmd = ACStartCommand(ac)

remote = RemoteControl()
remote.press(light_cmd)
remote.press(ac_cmd)

print("Undoing last command:")
remote.undo_last()
