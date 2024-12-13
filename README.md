# python_arduino
This is a project demonstrating the interaction of a Python program and an Arduino traffic light programmed in C++

To work, you need the pyserial library
To install, enter 'pip install pyserial' in the terminal (without quotes)

SKETCH FOR ARDUINO IN THE FOLDER sketch_sep28a
ALL ARDUINO PINOUTS ARE INDICATED AT THE BEGINNING OF THE SKETCH VIA #define

To configure the connection port, use config.py

You can find out which port your Arduino is connected to using the Arduino IDE:
https://www.flickr.com/photos/201988391@N06/54202269335/in/dateposted-public/ (picture)

Or using the test script in this folder called test.py. The output will look something like this:

Port check: COM1 (Serial port (COM1))
Port COM1 is available.
Port check: COM2 (Serial port (COM2))
Port COM2 is available.
Port check: COM3 (USB-SERIAL CH340 (COM3)) <<< HERE IS ARDUINO!!!
Port COM3 is available.

ATTENTION!!!! If suddenly your arduino IDE does not detect the board, try installing the driver from the driver.exe file!!!!
You need to press the INSTALL button. Administrator rights are required.
Link to virustotal: https://www.virustotal.com/gui/file/d12109675109512b6825c283e13f673b2f24f5e7e0791c1d64e73ebbeca263e2
