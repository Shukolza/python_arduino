from config import ARDUINO_PORT, BAUDRATE
import serial
from time import sleep
import tkinter
from tkinter import ttk
import webbrowser

LANGUAGE = str()

def contact_me():
    webbrowser.open('t.me/shukolza', new=2)

def send_delay():
    global arduino
    global delay_entry
    global status_label
    global LANGUAGE
    try:
        delay_ms = int(delay_entry.get()) * 1000
    except ValueError as exc:
        status_label.config(text=f"ОШИБКА! {exc}")
        return
    if delay_ms < 0:
        status_label.config(
            text=(
                "Задержка должна быть неотрицательной"
                if LANGUAGE == "RU"
                else "The delay must be non-negative"
            )
        )
        return
    command = (
        f"{delay_ms}\n"  # Добавляем символ новой строки для обозначения конца сообщения
    )
    arduino.write(command.encode())
    status_label.config(
        text=f"Отправлено: {delay_ms / 1000} с" if LANGUAGE == "RU" else f"{delay_ms}ms sent"
    )


def russian():
    global LANGUAGE
    choose_language.destroy()
    choose_language.quit()
    LANGUAGE = "RU"
    with open("language.txt", "w") as file:
        file.write(LANGUAGE)


def english():
    global LANGUAGE
    choose_language.destroy()
    choose_language.quit()
    LANGUAGE = "EN"
    with open("language.txt", "w") as file:
        file.write(LANGUAGE)


with open("language.txt", "r") as file:
    lang = file.read()
    if lang == "":
        choose_language = tkinter.Tk()
        choose_language.title("Choose language")
        choose_language.geometry("300x100")
        choose_language.iconbitmap('img/134948246.ico')

        languages_label = ttk.Label(
            choose_language, text="Choose language / Выберите язык"
        )
        russian_button = ttk.Button(choose_language, text="Русский", command=russian)
        english_button = ttk.Button(choose_language, text="English", command=english)

        languages_label.grid(column=0, row=0)
        russian_button.grid(column=0, row=1)
        english_button.grid(column=1, row=1)

        choose_language.mainloop()
    elif lang == "RU":
        LANGUAGE = "RU"
    else:
        LANGUAGE = "EN"

main_window = tkinter.Tk()
main_window.title("Управление arduino" if LANGUAGE == "RU" else "Arduino control")
main_window.geometry("800x600")
main_window.iconbitmap('img/134948246.ico')

delay_entry = ttk.Entry(main_window)
button_test = ttk.Button(
    main_window,
    text="Задать задержку" if LANGUAGE == "RU" else "Set delay",
    command=send_delay,
)
delay_entry.pack()
button_test.pack()

status_label = ttk.Label(main_window)
status_label.pack()

attention = ttk.Label(
    main_window,
    text=(
        "Задержку нужно вводить в секундах!"
        if LANGUAGE == "RU"
        else "The delay must be entered in seconds"
    ),
)
attention.pack()

contact_me = ttk.Button(text='Связаться с разработчиком' if LANGUAGE == 'RU' else 'Contact developer', command=contact_me)
contact_me.place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUDRATE, timeout=1)
    sleep(2)
    status_label.config(
        text="Подключено к Arduino" if LANGUAGE == "RU" else "Arduino connected"
    )
except serial.SerialException:
    status_label.config(
        text="Не удается подключиться!" if LANGUAGE == "RU" else "Can not connect!"
    )

main_window.mainloop()
