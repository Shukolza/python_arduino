# python_arduino

# This is a project demonstrating the interaction of a Python program and an Arduino traffic light programmed in C++

<p>To work, you need the <strong>pyserial </strong> library.<br>
To install, enter 'pip install pyserial' in the terminal (without quotes)</p>

<p>SKETCH FOR ARDUINO IN THE FOLDER <strong>'arduino_sketch'</strong><br>
ALL ARDUINO PINOUTS ARE INDICATED AT THE BEGINNING OF THE SKETCH VIA #define</p>

<p>To configure the connection port, use <strong>'config.py'</strong></p>

<p>You can find out which port your Arduino is connected to using the Arduino IDE:<br>
<img src="https://live.staticflickr.com/65535/54205673675_f46eb8a446.jpg">
</p>

<p>Or using the test script in this folder called test.py. The output will look something like this:<br>

Port check: COM1 (Serial port (COM1))<br>
Port COM1 is available.<br>
Port check: COM2 (Serial port (COM2))<br>
Port COM2 is available.<br>
Port check: COM3 (USB-SERIAL CH340 (COM3)) <<< <strong>HERE IS ARDUINO!!!</strong><br>
Port COM3 is available.<br>
</p>

<p>
If you want to reset the language selection, clear the <strong>"language.txt"</strong> file completely
</p>

<p><strong>ATTENTION!!!!</strong> If suddenly your arduino IDE does not detect the board, try installing the driver from the driver.exe<br>
You need to press the 'INSTALL' button. Administrator rights are required.<br>
Link to virustotal:<br> 
https://www.virustotal.com/gui/file/d12109675109512b6825c283e13f673b2f24f5e7e0791c1d64e73ebbeca263e2
</p>