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
```
[+] python fuzz.py --taget http://127.0.0.1/vuln --union-based
[+] python fuzz.py --taget http://127.0.0.1/vuln --string-based
```
![Screenshot (42)](https://user-images.githubusercontent.com/100557534/172825441-83673b46-bf1e-43bc-adfe-601336dedabc.png)
