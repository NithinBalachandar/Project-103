import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/nithi/Downloads"
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event.src_path+" has been created")
    def on_deleted(self,event):
        print(event.src_path+" has been deleted")
    def on_modified(self, event):
        print(event.src_path + " has been modified")
    def on_moved(self, event):
        print(event.src_path+ " has been moved")
eventHandler = FileMovementHandler()
observer = Observer()
observer.schedule(eventHandler, from_dir, recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt: 
    print("Stopped..")
    observer.stop()

    