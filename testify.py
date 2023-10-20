import time

project_time = int(input('Enter your desired time here')) # time to exam
for i in range(project_time, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print("Exam's time")
