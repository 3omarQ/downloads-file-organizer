from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil
path="C:\\Users\\LENOVO\\Downloads\\"
class DownloadHandler(FileSystemEventHandler):
    def on_download(self, event):
        # This method will be called whenever a file is created in the monitored folder

        downloaded_file_path = event.src_path
        file_extension = os.path.splitext(downloaded_file_path)[1]
        
        if(file_extension in [".jpg",".png",".gif",".jpeg"]):
            shutil.move(downloaded_file_path, path+"Images")
            print("file moved to images")

        if(file_extension in [".mp4",".mov",".avi",".mkv"]):
            shutil.move(downloaded_file_path, path+"Videos")
            print("file moved to videos")

        if(file_extension in [".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt"]):
            shutil.move(downloaded_file_path, path+"Documents")
            print("file moved to documents")

        if(file_extension in [".zip",".7z",".rar",".gz"]):
            shutil.move(downloaded_file_path, path+"Compressed")
            print("file moved to Compressed")

        if(file_extension in [".exe"]):
            shutil.move(downloaded_file_path, path+"Setups")
            print("file moved to Setups")

# Set up the observer to watch the Downloads folder

event_handler = DownloadHandler()
observer = Observer()
observer.schedule(event_handler, path=path,recursive=False)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
