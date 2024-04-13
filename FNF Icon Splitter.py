import os
import re
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image
import webbrowser
import requests
import sys

## Update Checking
def check_for_updates(current_version):
    try:
        response = requests.get('https://raw.githubusercontent.com/MeguminBOT/FNF-Icon-Splitter/main/latestVersion.txt')
        latest_version = response.text.strip()

        if latest_version > current_version:
            root = tk.Tk()
            root.withdraw()
            result = messagebox.askyesno("Update available", "An update is available. Do you want to download it now?")
            if result:
                print("User chose to download the update.")
                webbrowser.open('https://github.com/MeguminBOT/FNF-Icon-Splitter/releases/latest')
                sys.exit()
            else:
                print("User chose not to download the update.")
            root.destroy()
        else:
            print("You are using the latest version of the application.")
    except requests.exceptions.RequestException as err:
        print ("No internet connection or something went wrong, could not check for updates.")
        print ("Error details:", err)

current_version = '1.0.0'
check_for_updates(current_version)

## File processing
def count_png_files(input_dir):
    return sum(1 for filename in os.listdir(input_dir) if filename.endswith('.png'))

def sanitize_filename(name):
    return re.sub(r'[\\/:*?"<>|]', '_', name)

def select_directory(variable, label):
    directory = filedialog.askdirectory()
    if directory:
        variable.set(directory)
        label.config(text=directory)

## Extraction logic
def crop_transparency(image):
    image_alpha = image.convert("RGBA").split()[-1]
    bbox = image_alpha.getbbox()
    if bbox:
        return image.crop(bbox)
    return image

def split_icons(input_dir, save_location, progress_var, root):
    progress_var.set(0)
    total_files = count_png_files(input_dir)
    progress_bar["maximum"] = total_files

    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            full_path = os.path.join(input_dir, filename)
            spritesheet = Image.open(full_path)

            width, height = spritesheet.size
            frames = []
            for i in range(width // 150):
                for j in range(height // 150):
                    left = i * 150
                    upper = j * 150
                    right = left + 150
                    lower = upper + 150
                    frame = spritesheet.crop((left, upper, right, lower))
                    frames.append(frame)
                    
            cropped_frames = [crop_transparency(frame) for frame in frames]

            file_folder = sanitize_filename(os.path.splitext(filename)[0])
            file_save_location = os.path.join(save_location, file_folder)
            os.makedirs(file_save_location, exist_ok=True)
            for i, frame in enumerate(cropped_frames):
                frame_filename = f'frame_{i}.png'
                frame.save(os.path.join(file_save_location, frame_filename))
                progress_var.set((i + 1) / len(cropped_frames) * 100)
                root.update_idletasks()

    messagebox.showinfo("Information","Finished processing all files.")

## Graphical User Interface setup
root = tk.Tk()
root.title("FNF Icon Splitter")
root.geometry("480x320")

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, length=200, variable=progress_var)
progress_bar.pack(pady=8)

input_dir = tk.StringVar()
input_button = tk.Button(root, text="Select directory with icons", command=lambda: select_directory(input_dir, input_dir_label))
input_button.pack(pady=2)

input_dir_label = tk.Label(root, text="No input directory selected")
input_dir_label.pack(pady=4)

output_dir = tk.StringVar()
output_button = tk.Button(root, text="Select save directory", command=lambda: select_directory(output_dir, output_dir_label))
output_button.pack(pady=2)

output_dir_label = tk.Label(root, text="No output directory selected")
output_dir_label.pack(pady=4)

process_button = tk.Button(root, text="Start process", command=lambda: split_icons(input_dir.get(), output_dir.get(), progress_var, root))
process_button.pack(pady=8)

author_label = tk.Label(root, text="Tool written by AutisticLulu")
author_label.pack(side='bottom')

## Source Code
def contributeLink(url):
    webbrowser.open_new(url)

linkSourceCode = "https://github.com/MeguminBOT/FNF-Icon-Splitter"
link1 = tk.Label(root, text="If you wish to contribute to the project, click here!", fg="blue", cursor="hand2")
link1.pack(side='bottom')
link1.bind("<Button-1>", lambda e: contributeLink(linkSourceCode))

## Main loop
root.mainloop()
