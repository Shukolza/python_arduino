from config import ARDUINO_PORT, BAUDRATE
import serial
from time import sleep
import tkinter
from tkinter import ttk


def send_delay():
    delay_ms = int(delay_entry.get())
    if delay_ms < 0:
        status_label.config(text="Задержка должна быть неотрицательной")
        return
    command = (
        f"{delay_ms}\n"  # Добавляем символ новой строки для обозначения конца сообщения
    )
    arduino.write(command.encode())
    status_label.config(text=f"Отправлено: {delay_ms} мс")


main_window = tkinter.Tk()
main_window.title("Управление arduino")
main_window.geometry("800x600")

delay_entry = ttk.Entry()
button_test = ttk.Button(text="Задать задержку", command=send_delay)
delay_entry.pack()
button_test.pack()

status_label = ttk.Label()
status_label.pack()

attention = ttk.Label(text="Задержку нужно вводить в миллисекундах!")
attention.pack()

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUDRATE, timeout=1)
    sleep(2)
    status_label.config(text="Подключено к Arduino")
except serial.SerialException:
    status_label.config(text="Не удается подключиться")

print('GitHub test!')

main_window.mainloop()
