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
![Screenshot (41)](https://user-images.githubusercontent.com/100557534/172836079-eb08ec1d-20df-4b3d-9aed-451978549be7.png)
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
![Screenshot (44)](https://user-images.githubusercontent.com/100557534/172840484-2d251a6f-75f2-49d3-b727-18e44765ba58.png)
### RCE
choose rce fuzzer
```
[+] python fuzz.py --target http://127.0.0.1/vuln --RCE
```
![Screenshot (45)](https://user-images.githubusercontent.com/100557534/172838131-72313c91-1cc5-45c1-862a-a2596c7c3b62.png)
