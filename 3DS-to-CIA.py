import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
try:
    import tkinter
except ImportError:
    install("tkinter")
finally:
    from tkinter import *
    from tkinter import filedialog
    master = Tk()
    master.withdraw()
    def start():
        print("Starting...")
        subprocess.call([sys.executable, master.path23dsconv,'--overwrite','--boot9='+master.boot9,'--output='+master.ciadir, master.romdir+"/*.3ds"])
        input("Now check the output! Press any key to end.")
    master.romdir = filedialog.askdirectory(initialdir = "./",title = "Select directory containing ROMs...")
    master.ciadir = filedialog.askdirectory(initialdir = "./",title = "Select output directory...")
    master.path23dsconv = filedialog.askopenfilename(initialdir = "./",title = "Select 3dsconv.py",filetypes=[("3dsconv.py","*.py")])
    start()
	master.boot9 = filedialog.askopenfilename(initialdir = "./",title = "Select boot9.bin",filetypes=[("boot9.bin","*.bin")])
