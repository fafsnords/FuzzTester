# FuzzTester
### Introduction
**FuzzTester** is a pentesting tool that used for send a randomize payloads to trigger the vulnerability
### Installation
```
$ git clone https://github.com/fafsnords/FuzzTester

$ cd FuzzTester

$ pip install -r requirements

$ python fuzz.py
```
![Screenshot (41)](https://user-images.githubusercontent.com/100557534/172819368-7e9eb2d5-d4bf-45bc-a281-9fc6968f76e8.png)
### SQLi
you can choose the union based or string based method
```
[+] python fuzz.py --taget http://127.0.0.1/vuln --union-based
[+] python fuzz.py --taget http://127.0.0.1/vuln --string-based
```
![Screenshot (42)](https://user-images.githubusercontent.com/100557534/172829245-b23980d9-95d7-411c-89c4-58c3ac0b2390.png)
### XSS
![image](https://user-images.githubusercontent.com/100557534/172828595-b8cedac3-b63e-4ece-b46a-996078078a77.png)
