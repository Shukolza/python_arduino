Это проект, демонстрирующий взаимодействие программы на Python и светофора Arduino запрограммированного на C++

Для работы необходима библиотека pyserial
Чтобы установить введите в терминал 'pip install pyserial' (без кавычек)

СКЕТЧ ДЛЯ ARDUINO В ПАПКЕ sketch_sep28a
ВСЕ РАСПИНОВКИ ARDUINO УКАЗАНЫ В НАЧАЛЕ СКЕТЧА ЧЕРЕЗ #define

Для настройки порта подключения используйте config.py

Найти в какой порт у вас подключена Arduino вы можете используя Arduino IDE:
https://www.flickr.com/photos/201988391@N06/54202269335/in/dateposted-public/ (картинка)

Или используя тестовый скрипт в этой папке под названием test.py. Вывод будет выглядеть как то так:

Проверка порта: COM1 (Последовательный порт (COM1))
Порт COM1 доступен.
Проверка порта: COM2 (Последовательный порт (COM2))
Порт COM2 доступен.
Проверка порта: COM3 (USB-SERIAL CH340 (COM3)) <<< ВОТ И ARDUINO!!!
Порт COM3 доступен.

ВНИМАНИЕ!!!! Если вдруг ваша arduino IDE не обнаружает плату, попробуйте установить драйвер из файла driver.exe!!!!
Нужно нажать кнопку INSTALL. Нужны права администратора.
Ссылка на virustotal: https://www.virustotal.com/gui/file/d12109675109512b6825c283e13f673b2f24f5e7e0791c1d64e73ebbeca263e2