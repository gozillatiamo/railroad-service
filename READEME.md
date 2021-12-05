# Railroad Information Service

## Prerequisite
python3
for checking existing run this command.
```bash
python3 --version
```
if your machine not have one please check on this site depend on your OS.
https://www.python.org/downloads/



## Installation
It's up to you to use virtual env or not. If you don't want to use it just run
this command.
```bash
pip install -r requirements.txt
OR
python3 -m pip install -r requirements.txt
``` 
In case, you wanna use virtual env please follow these step.
### Install virtual env
```bash
python3 -m pip install virtualenv
```
from root project directory
```bash
virtualenv venv
```
### Activate virtual env
```bash
source venv/bin/activate
```
then install package with this command.
```bash
pip install -r requirements.txt
OR
python3 -m pip install -r requirements.txt
``` 
**During run tests script or runner script your need to activate virtual env.
### Deactivate(After you done with virtual env)
```bash
deactivate
```
## Running
```bash
./railroad
```
## Testing
```bash
./testsl.bash
```
