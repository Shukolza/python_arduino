import serial
import serial.tools.list_ports


def check_ports(timeout=1):
    """Проверяет доступность последовательных портов.

    Args:
        timeout: Таймаут в секундах для попытки открытия порта.
    """

    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print(f"Проверка порта: {port} ({desc})")
        try:
            with serial.Serial(
                port, baudrate=9600, timeout=timeout
            ) as ser:  # Используем произвольный baudrate, timeout важен
                print(f"Порт {port} доступен.")
        except serial.SerialException as e:
            print(f"Порт {port} недоступен: {e}")


if __name__ == "__main__":
    check_ports()
