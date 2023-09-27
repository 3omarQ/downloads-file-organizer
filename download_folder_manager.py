from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil

def get_available_file_name(file_path):
    base_name, extension = os.path.splitext(file_path)
    counter = 1

    while os.path.exists(file_path):
        file_path = f"{base_name} ({counter}){extension}"
        counter += 1

    return file_path

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        downloads_path = "C:\\Users\\LENOVO\\Downloads\\"
        downloaded_file_path = event.src_path
        file_extension = os.path.splitext(downloaded_file_path)[1]

        print(f"File downloaded: {downloaded_file_path}")
        
        categories = {
            ".jpg": "Images",
            ".png": "Images",
            ".gif": "Images",
            ".jpeg": "Images",
            ".mp4": "Videos",
            ".mov": "Videos",
            ".avi": "Videos",
            ".mkv": "Videos",
            ".pdf": "Documents",
            ".doc": "Documents",
            ".docx": "Documents",
            ".xls": "Documents",
            ".xlsx": "Documents",
            ".ppt": "Documents",
            ".pptx": "Documents",
            ".txt": "Documents",
            ".zip": "Compressed",
            ".7z": "Compressed",
            ".rar": "Compressed",
            ".gz": "Compressed",
            ".exe": "Setups",
        }

        if file_extension in categories:
            target_folder = os.path.join(downloads_path, categories[file_extension])
            new_file_path = os.path.join(target_folder, os.path.basename(downloaded_file_path))

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            if os.path.exists(new_file_path):
                new_file_path = get_available_file_name(new_file_path)

            shutil.move(downloaded_file_path, new_file_path)
            print(f"File moved to {categories[file_extension]} folder")

# Set up the observer to watch the Downloads folder

event_handler = DownloadHandler()
observer = Observer()
observer.schedule(event_handler, path=r"C:\Users\LENOVO\Downloads",recursive=False)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
