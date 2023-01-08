import subprocess
import shlex
import tkinter as tk
from tkinter import *
from subprocess import Popen, PIPE
from tkinter import simpledialog



root=tk.Tk()

#function definitions
def run_command(command):
    return Popen(command, 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                shell=False,
                cwd="C:\\iot_flasher")

def imei_pop():
    imei=simpledialog.askinteger(title="IMEI", prompt="Scan QR code")
    return imei
    
def btn_click():
    output_box.delete("1.0","end")
    if(iot_model.get() == "V3x Catacomb"):
        if (mode_selection.get() == 0):
            command = 'nrfjprog -d'
        elif (mode_selection.get() == 1):
            command = 'nrfjprog --eraseall'
        elif (mode_selection.get() == 2):
            command = 'nrfjprog --program "C:\\iot_flasher\catacomb-slim-prod.hex" --chiperase --reset --verify'
        with run_command(command) as p:
            if p.stdout:
                for line in p.stdout:
                    output_box.insert(END, line)
                    output_box.configure(background="green")
            if p.stderr:
                for line in p.stderr:
                    output_box.insert(END, line)
                    output_box.configure(background="red")
    
    elif (iot_model.get() != "V3x Catacomb"):
        imei=imei_pop()
        commands = ['nrfjprog --recover', 'nrfjprog --program "C:\\iot_flasher\wolfenstein-slim-prod.hex" --chiperase --verify', 'nrfjprog --rbp ALL', 'python3 "C:\\iot_flasher\provision.py" -d "C:\\iot_flasher\Wolfenstein_0222-2.csv" %s' %imei]
        commands = [shlex.split(x) for x in commands]
        outputs =[]
        for cmd in commands:
            outputs.append(subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate())
            for line in outputs:
                output_box.insert(END, line)
        
        



#window canvas creation
root.geometry("620x680")
root.configure(background="#F46C63")
root.resizable(False, True)
root.title("IOT Flasher")

#title
title=tk.Label(root)
title.grid(column="0", columnspan="3", pady="20", row="0")
title.configure(
            background="#F46C63",
            font="{Century Gothic} 24 {bold}",
            foreground="#ffffff",
            text="IOT FLASHER",
        )

#warning message
caution=tk.Label(root)
caution.grid(column="0", columnspan="3", pady="10",padx="10", row="1")
caution.configure(
            background="#F46C63",
            font="{Century Gothic} 22 {bold}",
            foreground="#000000",
            text="IMPORTANT! CHECK IOT MODEL",
        )

#iot model selection
model_selection=tk.Label(root)
model_selection.grid(column="1", row="2", sticky="e", pady="20")
model_selection.configure(
            background="#F46C63",
            font="{Microsoft YaHei} 12 {bold}",
            text="Select IOT Model",
        )

#dropdown menu
options=[
    "V3x Catacomb",
    "V3x Wolfestein",
    "V4  Wolfestein"
]
iot_model = StringVar()
iot_model.set(options[0])

drop= OptionMenu(root, iot_model,*options)
drop.grid(column="2",sticky="w", padx="15", row="2")

#radio buttons
mode_selection=IntVar()
modes=["reboot","Erase Firmware", "Flash Firmware"]

for index in range(len(modes)):
    radiobutton= Radiobutton(root, text=modes[index], variable=mode_selection, value=(index), background="#F46C63", font=("Century Gothic", 12))
    radiobutton.grid(column=index, padx="5", pady="15", row="3")

#proceed button
btn=Button(root, text="Proceed", command=btn_click)
btn.grid(column="0", columnspan="3", row="5",padx=15, pady=10)

#output box
output_box=tk.Text()
output_box.configure(height="20", width="70")
output_box.grid(column="0", columnspan="3", pady="15", padx="25", row="6")
output_box.bind("<Key>", lambda e: "break")


root.mainloop()