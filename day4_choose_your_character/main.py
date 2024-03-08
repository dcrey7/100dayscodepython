
import os
import time
import keyboard
import cyf_art as cyf_art

def clear_screen():
    # Check if the system is Windows or Linux and clear the screen accordingly
    os.system('cls' if os.name == 'nt' else 'clear')

filenames = cyf_art.art

def animator(filenames, delay):
    frames = filenames
    while True:
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            clear_screen()  # Clear the screen after each frame
            
            # Check for keypress to stop animation and display the selected ASCII art
            print("Press any key to chose your art")
            if any(keyboard.is_pressed(chr(key)) for key in range(32, 127)):
                clear_screen()
                print("".join(frame))
                return  # Exit the function when any key is pressed

animator(filenames, 0.1)
