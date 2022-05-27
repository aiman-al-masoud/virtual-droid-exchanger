import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
#https://thepythoncorner.com/posts/2019-01-13-how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/

class WatchDog(Observer):

    def __init__(self):
        Observer.__init__(self)

    def get(path, **kwargs):
        params = {"on_created" : lambda e: print("created", e.src_path) , "on_deleted" :  lambda e: print("deleted", e.src_path), "on_modified" :  lambda e: print("modified", e.src_path), "on_moved":  lambda e: print("moved", e.src_path)}
        params.update(kwargs)
        
        patterns = ["*"]
        ignore_patterns = None
        ignore_directories = False
        case_sensitive = True
        my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

        my_event_handler.on_created = params["on_created"]
        my_event_handler.on_deleted = params["on_deleted"]
        my_event_handler.on_modified = params["on_modified"]
        my_event_handler.on_moved = params["on_moved"]

        go_recursively = True
        my_observer = WatchDog()
        my_observer.schedule(my_event_handler, path, recursive=go_recursively)
        return my_observer
