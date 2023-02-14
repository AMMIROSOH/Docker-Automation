<h1 align="center">Docker Run Automation with python (AutoRun)</h1>

## ✨ Prepairing

- Install Docker and deploy your image.
- make a container for your image (once in whole deployment).
- install python(any version).

## ⭐️ Initialize

in `DockerAutorun.py` set `DOCKER_PATH` to directory of your installed docker app, and `CONTAINER_ID` to the id of your container you want to autorun (two first characters are enough).
```python
DOCKER_PATH = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
CONTAINER_ID = "c4"
```

## ➕ Running any application on startup

you can start your applications by adding them to this section.

```python
os.system(f"start cmd /k docker exec -it {CONTAINER_ID} bash rundjango.sh")
os.system(f"start cmd /k docker exec -it {CONTAINER_ID} bash rundreact.sh")
os.system(f"start cmd /k docker exec -it {CONTAINER_ID} bash runocrservice.sh")
```
three sample `React`, `Django`, `pure Python` applications.

but before using this part you have to make `.sh` bash files to run the apps, for this simply execute:
```bash
nano rundjango.sh
```
or (in case which one you have installed):
```bash
vim rundjango.sh
```
and write this commands for these examples to the file.

for `Django` Application:
```bash
python manage.py runserver 0.0.0.0:8000
```

for `React` Application in custom directory:
```bash
npm start --prefix my-app/
```

for `python` Application in custom directory :
```bash
cd ocrservice && python main.py
```

👉 `&&` runs second command in the new set directory.

## 🚀 Run

now you can use your application with only one click on `AutoRun.bat`.

and type `exit` in lowercase to stop the whole container.

👉 if you just close the console, container and it apps will continue running and you most rerun the `.bat` file to close all apps and running instances of container then entering `exit` again to fully close the application.
