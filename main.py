import random
import subprocess
import sys
import time



x = 0



print("Выберите:")
print("1. Мультипоточная работа")
print("2. Однопоточная работа")
i = 2

if i == '1':
    print("MULTITHREAD ACTIVATED")
    times = time.time()
    while True:
        x += 1
        process = subprocess.Popen([sys.executable, "RunBots.py"])
        process.wait()
        print(f"Отдыхаем 60 секунд")
        time.sleep(60)
        process = subprocess.Popen([sys.executable, "TestMessagingWithBots.py"])
        process.wait()
        if x % 5 == 0:
            print(f"Отдыхаем 60 секунд перед заданием на вход в каналы")
            time.sleep(60)
            process = subprocess.Popen([sys.executable, "JoinChannelsTests.py"])
            process.wait()


        print(f"Успешно Круг:{x}")
        print(f"Время:{time.time() - times}")
        if x % 10 == 0:
            free_time = random.randrange(300, 1200)
            print(f"Успешно отдыхаем {600 + free_time}")
            time.sleep(free_time + 600)

        if time.time() - times > 6000:
            print('Проверка баланса')
            process = subprocess.Popen([sys.executable, "Checkbalance.py"])
            process.wait()
            times = time.time()
else:
    times = time.time()
    print("SOLO THREAD ACTIVATED")
    while True:
        x += 1
        process = subprocess.Popen([sys.executable, "RunBotsSoloThread.py"])
        process.wait()
        print(f"Отдыхаем 15 секунд")
        time.sleep(15)
        process = subprocess.Popen([sys.executable, "MessagingWithBotsSoloThread.py"])
        process.wait()
        if x % 5 == 0:
            print(f"Отдыхаем 60 секунд перед заданием на вход в каналы")
            time.sleep(120)
            process = subprocess.Popen([sys.executable, "JoinChannelsSoloThread.py"])
            process.wait()


        print(f"Успешно Круг:{x}")
        print(f"Время:{time.time() - times}")
        if x % 10 == 0:
            free_time = random.randrange(120, 300)
            print(f"Успешно отдыхаем {200 + free_time}")
            time.sleep(free_time + 200)

        if time.time() - times > 6000:
            print('Проверка баланса')
            process = subprocess.Popen([sys.executable, "Checkbalance.py"])
            process.wait()
            times = time.time()




