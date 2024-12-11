# MY_AI TOOLS or mai_tools
Set of tools created for and with AI

## Tools: 
## 1. Perpetual Calendar offline
Just pick a month and a year and print a proper calendar and days
```python
Introduce el número de mes (1-12): 1
Introduce el año (ej. 2023): 2025
Calendario de January 2025:
L  M  M  J  V  S  D
       1  2  3  4  5 
 6  7  8  9 10 11 12 
13 14 15 16 17 18 19 
20 21 22 23 24 25 26 
27 28 29 30 31
```
## 2. Horizontal Calendar
Just a calendar that shows the days of the month horizontally.
## 3. TBD


# General setup:

### A. Create a venv and activate it:

```shell
 pyenv virtualenv -p python3.10 env_mai_tools
```
Alternatively, you can use the following command to activate the venv:
```shell
venv env_mai_tools
source env_mai_tools/bin/activate
```

### B. Install the requirements: 
```shell
pip install -r requirements.txt
```

### C. Fill the .env if needed: 
```
APIKEY=xxxxx
URL=xxx.com
```
    
### D. Run the .py
```shell
python <My_AI_Tool>.py
```

### E. Check the results & enjoy 
```shell
```

### Issues with the webdriver? try updating to the last version of the chromedriver:

```shell
pip install --upgrade webdriver-manager selenium
```
