import subprocess
import sys
import random
import time
import datetime
from playsound import playsound

x = 0
times = time.time()
print(f"Подготовка...")
time.sleep(3)
print(f"Ready")
time.sleep(1)
print(f"Steady")
time.sleep(1)
print(f"Готов вкалывать")
playsound('readytowork.mp3')

while True:
    x += 1
    process = subprocess.Popen([sys.executable, "RunBots.py"])
    process.wait()
    process = subprocess.Popen([sys.executable, "TestMessagingWithBots.py"])
    process.wait()
    process = subprocess.Popen([sys.executable, "JoinChannelsTests.py"])
    process.wait()
    print(f"Успешно Круг:{x}")
    print(f"Время:{time.time() - times}")
    if x % 10 == 0:
        free_time = random.randrange(300, 1200)
        print(f"Успешно отдыхаем {600 + free_time}")
        time.sleep(free_time + 60)

    if time.time() - times > 6000:
        print('Проверка баланса')
        process = subprocess.Popen([sys.executable, "Checkbalance.py"])
        process.wait()
        times = time.time()


