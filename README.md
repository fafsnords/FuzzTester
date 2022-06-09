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
choose xss fuzzer
```
[+] python fuzz.py --target http://127.0.0.1/vuln --XSS
```
![Screenshot (43)](https://user-images.githubusercontent.com/100557534/172829567-9fa09907-2e4f-474a-82d9-2c39a31e9c06.png)
### LFI
choose lfi fuzzer
```
[+] python fuzz.py --target http://127.0.0.1/vuln --LFI
```
![Screenshot (44)](https://user-images.githubusercontent.com/100557534/172831528-646090f2-a6ac-46ba-9e03-21d1f7c4d774.png)
### RCE
choose rce fuzzer
```
[+] python fuzz.py --target http://127.0.0.1/vuln --RCE
```
