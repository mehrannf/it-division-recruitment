import os
import fpp

# Trying to defie the path
PIPE_PATH = "/tmp/my_named_pipe"

class MessageListener(fpp.Listener):
    """ Custom listener to handle messages received from the peripheral. """
    
    def on_message_received(self, msg):
        print(f"Received from peripheral: {msg}")
        # Write the received message to the pipe
        with open(PIPE_PATH, "w") as pipe:
            pipe.write(msg + "\n") 

def main():
    device_path = "/dev/ttyUSB0"
    peripheral = fpp.Peripheral(device_path)
    listener = MessageListener()
    notifier = fpp.Notifier(peripheral, [listener])

    print("Listening to the peripheral...")
    notifier.start_reading()  # This should trigger message reception

if __name__ == "__main__":
    # Ensure the pipe exists
    if not os.path.exists(PIPE_PATH):
        os.mkfifo(PIPE_PATH)

    main()
