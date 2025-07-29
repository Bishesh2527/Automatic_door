from transitions import Machine
import time
import threading

# The door has 4 moods (states)
states = ['closed', 'opening', 'open', 'closing']

# This is like building the robot door
class AutomaticDoor:
    def __init__(self):
        # Start with the door closed
        self.machine = Machine(model=self, states=states, initial='closed')

        # If someone comes, start opening the door
        self.machine.add_transition(trigger='someone_comes', source='closed', dest='opening', before='open_door')

        # When the door is fully open
        self.machine.add_transition(trigger='door_done_opening', source='opening', dest='open', before='say_door_open')

        # Wait a bit, then close
        self.machine.add_transition(trigger='no_one_here', source='open', dest='closing', before='close_door')

        # Once door is closed
        self.machine.add_transition(trigger='door_done_closing', source='closing', dest='closed', before='say_door_closed')

    # These are just the robot's messages
    def open_door(self):
        print("🤖 Opening the door...")
        # Automatically move to open state after a brief moment
        threading.Timer(1.0, self.door_done_opening).start()

    def say_door_open(self):
        print("🤖 Door is fully open!")
        print("🤖 Door will stay open for 5 seconds...")
        # Keep door open for 5 seconds, then close
        threading.Timer(5.0, self.no_one_here).start()

    def close_door(self):
        print("🤖 Closing door in 3 seconds...")
        time.sleep(3)
        print("🤖 Closing the door...")
        # Automatically move to closed state after closing
        threading.Timer(1.0, self.door_done_closing).start()

    def say_door_closed(self):
        print("🤖 Door is fully closed!")
    
    def activate_door(self):
        """Activate the door opening sequence"""
        if self.state == 'closed':
            self.someone_comes()
        else:
            print(f"🤖 Door is currently {self.state}. Please wait...")

# Interactive door control
door = AutomaticDoor()

print("🚪 Automatic Door Control System")
print("Press 1 to activate the door, or 'q' to quit")

while True:
    user_input = input("\nEnter command: ").strip()
    
    if user_input == '1':
        door.activate_door()
    elif user_input.lower() == 'q':
        print("🤖 Shutting down door system. Goodbye!")
        break
    else:
        print("🤖 Invalid command. Press 1 to activate door or 'q' to quit.")