import os

# Define a named pipe path
PIPE_PATH = "/tmp/my_named_pipe"

def read_from_pipe():
    """ Reads and prints messages received from the named pipe. """
    print("Waiting for messages...")

    while True:
        with open(PIPE_PATH, "r") as pipe:
            msg = pipe.readline().strip()
            if msg:
                print(f"Received message: {msg}")

if __name__ == "__main__":
    # Ensure the named pipe exists
    if not os.path.exists(PIPE_PATH):
        os.mkfifo(PIPE_PATH)

    read_from_pipe()
