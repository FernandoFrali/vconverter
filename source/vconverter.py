import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def select_files():
    print("Select the files to convert.")
    root = tk.Tk()
    root.withdraw()

    files = filedialog.askopenfilenames(title="Select files to convert")

    for file in files:
        if file.endswith(".ts") or file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".avi"):
            continue
        else:
            print("Invalid file type. Select files with '.ts', '.mkv', '.mp4' or '.avi' extension.")
            return None

    return files

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def select_type():
    clean_screen()
    print("-----------------")
    print("Select the type of conversion:")
    print("1: to .mkv")
    print("2: to .mp4")
    print("3: to .avi")
    print("-----------------")
    option = int(input("> "))
    if option == 1:
        return "mkv"
    elif option == 2:
        return "mp4"
    elif option == 3:
        return "avi"
    else:
        print("Invalid option.")
        return None

def convert_ts_to_mkv():
    input_files = select_files()
    output_type = select_type()

    for file in input_files:
        input_type = file.split(".")[-1]
        output_file = file.replace(input_type, output_type)
        ffmpeg_path = "../ffmpeg/ffmpeg.exe"

        try:
            subprocess.run([ffmpeg_path, "-i", file, "-c", "copy", output_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        convert_ts_to_mkv()
    except KeyboardInterrupt:
        print("Operation canceled by user.")
    except Exception as e:
        print(f"")
