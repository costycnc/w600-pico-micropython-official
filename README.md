# w600-pico micropython official

I find micropython source code here https://github.com/robert-hh/Micropython-Editor

Official store https://www.wemos.cc/en/latest/w600/index.html

Another platforms

Arduino     https://github.com/w600/arduino

           arduino http://arduino.w600.fun/package_w600_index.json 
           
PlatformIO   https://github.com/maxgerhardt/platform-w60x            

---

MicroPython Documentation Release 1.10 https://docs.micropython.org/en/v1.10/micropython-docs.pdf

---

Bellow how use preinstalled micropython
       
You can use this terminal for write(comunicate) with w600-pico https://bipes.net.br/aroca/web-serial-terminal/ 

Paste in terminal with ctrl+A+V
        
    import easyw600
    easyw600.createap(ssid="W600_softAP")        
    import w600
    w600.run_ftpserver(port=21,username="user",password="12345678")
    
        
after send these four lines if not have a ftp you can use dos command prompt >> ftp 192.168.43.1

will see 
        
        Connected to 192.168.43.1.
        220-= welcome on W600 FTP server =-
        220
        
        or...
        
install https://filezilla-project.org/download.php?type=client

        and connect at 192.168.43.1 user 12345678
        and will see all files and folders from w600-pico
        Keep in mind ... is a local connection ... so need to discconect from router and connect to "W600_softAP" station
        
        
with mu editor https://github.com/mu-editor/mu/releases/tag/1.1.0-alpha.2
this did about alpha.2 ... i not understand how appear w600 in listing ... i download but not appear ... need to study this topic https://forum.micropython.org/viewtopic.php?t=8503

also a good tutorial https://www.sigmdel.ca/michel/ha/w600/first_look_w600_en.html

> vshymanskyy  Firmware upload tool for Winner Micro W600 & W601 WiFi  https://github.com/vshymanskyy/w600tool
> 
> windows executable https://github.com/vshymanskyy/w600tool/releases/tag/0.1



https://docs.micropython.org/en/v1.8.2/esp8266/esp8266/tutorial/filesystem.html

           >>> w600.flash_size()                                                                                                                                 
           1048576 

           >>> import gc                                                                                                                                         
           >>> gc.mem_free()                                                                                                                                     
           44160                                                                                                                                                 
           >>> gc.collect()                                                                                                                                      
           >>> gc.mem_free()                                                                                                                                     
           44768                                                                                                                                                 
           >>>     

        >>> import os
        >>> os.listdir()
        ['sys', 'lib', 'cert', 'boot.py', 'main.py', 'easyw600.py']
        
        
        write:
        >>> f = open('data.txt', 'w')
        >>> f.write('some data')
        9 
        >>> f.close()
        
        
        append:
        >>> f = open('data.txt', 'a')
        >>> f.write('some data')
        9 
        >>> f.close()
        
        --------------------------------------------------
        >>> f=open('main.py','w')
        >>> f.write('print("Costycnc foam cutter")')
        13
        >>> f.close()
        >>> f=open('main.py')
        >>> f.read()
        'print("aaaa")'
         >>> 
         
         RESET
    __            __
    \ \    /\    / /
     \ \  /  \  / /
      \ \/ /\ \/ / 
       \  /  \  /
       / /\  / /\ 
      / /\ \/ /\ \ 
     / /  \  /  \ \ 
    /_/    \/    \_\ 



    WinnerMicro W600
    Costycnc foam cutter <------
    MicroPython v1.10-282-g6a9b3cb-dirty on 2019-09-17; WinnerMicro module with W600
    Type "help()" for more information.
    
        -----------------------------------------------------------------
        
If want write to main.py multilines (with https://bipes.net.br/aroca/web-serial-terminal/ ) in one command like 
     
       f=open('main.py','w')
       f.write('print("1234") \r print("5678")')
       f.close()
       
       use \r or maybe \r\n after any line same as example below
        
For exampme if you want write code in main.py that connect and create ftp server automatically same as this code 

        import easyw600
        easyw600.createap(ssid="W600_softAP")
        import w600
        w600.run_ftpserver(port=21,username="user",password="12345678")
        
you can write:

        f.write('import easyw600 \r easyw600.createap(ssid="W600_softAP") \r import w600 \r w600.run_ftpserver(port=21,username="user",password="12345678")')
        
and will see  that working ... but how did is better if put \r\n how find in many examples     

---------------------------------------------------------------------------------------------------------

another sdk for testing  https://www.keil.com/demo/eval/arm.htm#!#DOWNLOAD

https://docs.wiznet.io/img/products/wizfi360/board/wizfi360sdk/wizfi360_w600_sdk_guide_v0.0.1_e.pdf

https://docs.wiznet.io/Product/Wi-Fi-Module/WizFi360/Other-Resource/w600_sdk

file:///C:/Keil_v5/ARM/HLP/Release_Notes.htm  

https://github.com/flyingcys/w600  for keil
