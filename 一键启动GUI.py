import subprocess

def start_gui_program():
    try:
        subprocess.Popen(["python", "MirageTankGo.py", "--gui"])
    except FileNotFoundError:
        print("Error: Python interpreter not found. Make sure Python is installed and in your PATH.")

if __name__ == "__main__":
    start_gui_program()
