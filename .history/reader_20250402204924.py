import os
import fpp

# Define a named pipe path
PIPE_PATH = "/tmp/my_named_pipe"

class MessageListener(fpp.Listener):
    """ Custom listener to handle messages received from the peripheral. """
    
    def on_message_received(self, msg):
        print(f"Received from peripheral: {msg}")  # Debugging
        # Write the received message to the named pipe
        with open(PIPE_PATH, "w") as pipe:
            pipe.write(msg + "\n")  # Ensure new line separation

def main():
    device_path = "/dev/some_device"  # Change this to the actual device path
    peripheral = fpp.Peripheral(device_path)
    listener = MessageListener()
    notifier = fpp.Notifier(peripheral, [listener])

    print("Listening to the peripheral...")
    notifier.start_reading()  # This should trigger message reception

if __name__ == "__main__":
    # Ensure the named pipe exists
    if not os.path.exists(PIPE_PATH):
        os.mkfifo(PIPE_PATH)

    main()
