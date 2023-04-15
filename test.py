import ctypes
from sys import platform
import os
import win32api
import win32con
import time

BASEDIR = os.getcwd()
dll_name = r'C:\Users\sarwa\Documents\text_extract_cpp\firstDLL.dll'
# dll_handle = win32api.LoadLibraryEx(dll_name, 0, win32con.LOAD_WITH_ALTERED_SEARCH_PATH)
dll_handle = win32api.LoadLibraryEx(dll_name, 0, win32con.LOAD_WITH_ALTERED_SEARCH_PATH)

try:
    st_time = time.time()
    check = ctypes.WinDLL(dll_name, handle=dll_handle)
    print("Successfully loaded ", check)
    path = r"C:\Users\sarwa\Documents\text_extract_cpp\images"
    
    for file in os.listdir(path):
        fulpath = os.path.join(path, file)
        result =check.get_bbox(fulpath.encode('utf-8'))

    end_time = time.time()
    total_time = end_time-st_time
    print(f"total time taken: {total_time}")
except Exception as e:
    print(e)