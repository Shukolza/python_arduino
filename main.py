from config import ARDUINO_PORT, BAUDRATE
import serial
from time import sleep
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from tkinter import PhotoImage

language = str()

def set_icon(window: tk.Tk) -> None:
    try:
        icon = PhotoImage(file="img/134948246.png")
        window.iconphoto(False, icon)
    except Exception as e:
        print(f"ERROR installing icon: {e}" if language == 'EN' else f'ОШИБКА установки иконки: {e}')


def contact_me():
    """Opens my telegram in browser"""
    webbrowser.open("t.me/shukolza", new=2)


def send_delay():
    """Sends delay to the arduino with serial port"""
    global arduino
    global delay_entry
    global status_label
    global language
    try:
        delay_ms = int(delay_entry.get()) * 1000
    except ValueError as exc:
        messagebox.showerror( # type: ignore
            title="ОШИБКА" if language == "RU" else "ERROR",
            text=f"ОШИБКА! {exc}" if language == "RU" else f"ERROR! {exc}",
        )
        return
    if delay_ms < 0:
        messagebox.showerror( # type: ignore
            title="ОШИБКА" if language == "RU" else "ERROR",
            text=(
                "Задержка должна быть неотрицательной"
                if language == "RU"
                else "The delay must be non-negative"
            ),
        )
        return
    command = (
        f"{delay_ms}\n"  # Добавляем символ новой строки для обозначения конца сообщения
    )
    arduino.write(command.encode())
    messagebox.showinfo( # type: ignore
        title="УСПЕШНО" if language == "RU" else "SUCCESSFUL",
        text=(
            f"Отправлено: {delay_ms / 1000} с"
            if language == "RU"
            else f"{delay_ms}ms sent"
        ),
    )


def russian():
    """Sets language to russian"""
    global language
    choose_language.destroy()
    choose_language.quit()
    language = "RU"
    with open("language.txt", "w") as lang_file:
        lang_file.write(language)


def english():
    """Sets language to english"""
    global language
    choose_language.destroy()
    choose_language.quit()
    language = "EN"
    with open("language.txt", "w") as lang_file:
        lang_file.write(language)


with open("language.txt", "r") as file:
    lang = file.read()
    if lang == "":
        choose_language = tk.Tk()
        choose_language.title("Choose language")
        choose_language.geometry("300x100")
        set_icon(choose_language)

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
        language = "RU"
    else:
        language = "EN"

main_window = tk.Tk()
main_window.title("Управление arduino" if language == "RU" else "Arduino control")
main_window.geometry("800x600")
set_icon(main_window)

delay_entry = ttk.Entry(main_window)
button_test = ttk.Button(
    main_window,
    text="Задать задержку" if language == "RU" else "Set delay",
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
        if language == "RU"
        else "The delay must be entered in seconds"
    ),
)
attention.pack()

contact_me = ttk.Button(
    text="Связаться с разработчиком" if language == "RU" else "Contact developer",
    command=contact_me,
) # type: ignore
contact_me.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se") # type: ignore

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUDRATE, timeout=1)
    sleep(2)
    messagebox.showinfo( # type: ignore
        title="УСПЕШНО" if language == "RU" else "SUCCESSFUL",
        text="Подключено к Arduino" if language == "RU" else "Arduino connected",
    )
except serial.SerialException:
    messagebox.showerror( # type: ignore
        title="ERROR" if language == "EN" else "ERROR",
        message=(
            "Не удается подключиться к Arduino"
            if language == "RU"
            else "Can not connect to Arduino"
        ),
    )

main_window.mainloop()
