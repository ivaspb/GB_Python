import time
time_sec = int(input('Укажите время в секундах: '))
time_full = time.strftime('%H:%M:%S', time.gmtime(time_sec))

print('В часах, минутах и секундах это:',time_full)
