# IoT Flasher 🔌💻
IoT Flasher is a Python script that simplifies the process of flashing firmware onto IoT boards in scooters 🛴. The script automates the execution of terminal commands and provides visual cues 🟢🟡🔴 to indicate the success or failure of the operation.

The purpose of this program is to provide a user-friendly interface for mechanics to perform various actions related to flashing firmware onto IoT boards in scooters. The program automates the execution of terminal commands and provides visual cues to indicate the success or failure of the operation, which can make it easier for mechanics who may not be comfortable using the command line to fix issues with IoT boards independently. The program supports multiple modes of operation, including detecting the connected IoT board, erasing the firmware on the IoT board, and flashing new firmware onto the IoT board. This can help to streamline the process of troubleshooting and repairing IoT-related issues in scooters, improving efficiency and reducing downtime.

<img src=".\iot_flasher_GUI.png" width="450" height="500"/>

## Technologies used 💻
* Python 3 🐍
* Tkinter library 🎨
* nrfjprog 🛠

# How to use 🤔
1. Install the required libraries and dependencies.
2. Clone or download this repository to your local machine.
3. Run the script with the command python iot_flasher.py.
4. Select the appropriate IoT model from the drop-down menu.
5. Select the desired mode of operation from the drop-down menu.
6. Click the "Run" button to execute the terminal commands.
7. The output of the terminal commands will be displayed in the text box. A green background 🟢 indicates a successful operation, while a red background 🔴 indicates an error.

# Disclaimer ⚠️🔒
Some of the files required to run this program, such as the firmware hex files and provisioning script, are owned by the rental scooter company and are considered private and non-disclosable information. As a result, these files are not included in this repository. The code provided here is for reference only and may not be fully functional without the required files.

# Modes of operation 🔄
* Detect: Detects the connected IoT board. 🕵️‍♂️
* Erase: Erases the firmware on the IoT board. 🧹
* Flash: Flashes new firmware onto the IoT board. 💾

# Troubleshooting ❓
If you encounter any issues while using this script, please check the output in the text box for error messages. You can also try running the terminal commands manually to troubleshoot the issue. 🤔
