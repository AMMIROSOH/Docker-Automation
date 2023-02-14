import os
from time import sleep
import atexit

def exit_handler():
    os.popen("docker stop " + CONTAINER_ID).read()
atexit.register(exit_handler)


# Config
DOCKER_PATH = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
CONTAINER_ID = "c4"

# Const
DOCKER_RUN_STR = "CONTAINER ID"

# Openning Docker app
while True:
    os.startfile(DOCKER_PATH)
    dockerIsRunning = os.popen("docker ps").read()
    if DOCKER_RUN_STR in dockerIsRunning:
        break
    else:
        print("Docker Deamon not Running Trying after 20 Seconds.")
        sleep(20)
print("Docker Deamon is Running.")

# Starting Docker container
os.popen("docker stop " + CONTAINER_ID).read()
containerIsRunning = os.popen("docker start " + CONTAINER_ID).read()
if containerIsRunning == CONTAINER_ID+'\n':
    print(f"Docker Container {CONTAINER_ID} is running.")

# Starting custom apps
os.system(f"start cmd /k docker exec -it {CONTAINER_ID} bash rundjango.sh")
os.system(f"start cmd /k docker exec -it {CONTAINER_ID} bash rundreact.sh")
os.system(f"start cmd /k docker exec -it {CONTAINER_ID} bash runocrservice.sh")

# Listening for Exit
while True:
    command = input("Enter exit: ")
    if command=="exit":
        os.popen("docker stop " + CONTAINER_ID).read()
        print("Everything stopped.")
        break