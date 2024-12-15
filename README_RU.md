# python_arduino

# Это проект, демонстрирующий взаимодействие программы на Python и светофора Arduino запрограммированного на C++

<p>Для работы необходима библиотека <strong>pyserial</strong><br>
Чтобы установить введите в терминал 'pip install pyserial' (без кавычек)</p>

<p>СКЕТЧ ДЛЯ ARDUINO В ПАПКЕ <strong>'arduino_sketch'</strong><br>
ВСЕ РАСПИНОВКИ ARDUINO УКАЗАНЫ В НАЧАЛЕ СКЕТЧА ЧЕРЕЗ #define </p>

<p>Для настройки порта подключения используйте <strong>'config.py'</strong></p>

<p>
Найти в какой порт у вас подключена Arduino вы можете используя Arduino IDE:<br>
<img src="https://live.staticflickr.com/65535/54205673675_f46eb8a446.jpg">
</p>

<p>Или используя тестовый скрипт в этой папке под названием test.py. Вывод будет выглядеть как то так:<br>

Проверка порта: COM1 (Последовательный порт (COM1))<br>
Порт COM1 доступен.<br>
Проверка порта: COM2 (Последовательный порт (COM2))<br>
Порт COM2 доступен.<br>
Проверка порта: COM3 (USB-SERIAL CH340 (COM3)) <<< <strong>ВОТ И ARDUINO!!!</strong><br>
Порт COM3 доступен.<br>
</p>

<p>
Если вы хотите сбросить выбор языка, полностью очистите файл <strong>"language.txt"</strong>
</p>

<p>ВНИМАНИЕ!!!! Если вдруг ваша arduino IDE не обнаружает плату, попробуйте установить драйвер из файла driver.exe<br>
Нужно нажать кнопку 'INSTALL'. Нужны права администратора.<br>
Ссылка на virustotal:<br>
https://www.virustotal.com/gui/file/d12109675109512b6825c283e13f673b2f24f5e7e0791c1d64e73ebbeca263e2
</p>
