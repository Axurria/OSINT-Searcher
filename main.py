import subprocess
import requests
import json
import webbrowser

# Config
leakcheckAPI = None # Enter here your API Key if you want to use leakcheck.io for searching :)

# Header
name = """
                         .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||          OSINT Tool By Axurria
         !.........||||                     ||||          
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb.... 
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.  
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!  
          `..::!8888888888888888888888888888888899fT|!^"'   
            `' !!988888888888888888888888899fT|!^"' 
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'

[+]Made with love by @Axurria - https://vacban.wtf
"""
print(name)
print("-----------------------------")
print("[+]Modules available")
print("-----------------------------")
print(" >[1]Full Name lookup")
print(" >[2]Nickname lookup")
print(" >[3]Email lookup")
print(" >[4]Phone lookup")
print(" >[5]Adress lookup")
print(" >[6]Photo search")
print(" >[7]MAC Address Lookup")
print(" >[8]Website Lookup")
print(" >[9]Leak Search")
print("-----------------------------")
print("[+]Open your default browser")
print("-----------------------------")

# Modules
option = input("[+]Select option: ")
print("-----------------------------")
if (option == "1"):
    webbrowser.open('https://www.whitepages.com/', new=2)
    webbrowser.open('https://www.truepeoplesearch.com/', new=2)
    webbrowser.open('https://www.zabasearch.com/', new=2)
    webbrowser.open('https://www.spokeo.com/people-search', new=2)
    webbrowser.open('https://www.411.com/person', new=2)
    webbrowser.open('https://publicrecords.directory/', new=2)
    webbrowser.open('https://www.intelius.com/', new=2)
if(option == "2"):
    option = input("[+]Enter nickname: ")
    webbrowser.open('https://checkusernames.com/', new=2)
    if(leakcheckAPI is not None):
        webbrowser.open("https://leakcheck.net/api/public?key="+ leakcheckAPI +"&check=" + option, new=2)
    p = subprocess.Popen(["start", "cmd", "/k", "py sherlock/sherlock.py " + option], shell = True)
    p.wait()
if(option == "3"):
    if(leakcheckAPI is not None):
        option = input("[+]Enter email: ")
        webbrowser.open("https://leakcheck.net/api/public?key="+ leakcheckAPI +"&check=" + option, new=2)
    webbrowser.open('https://epieos.com', new=2)
    webbrowser.open('https://com.lullar.com/', new=2)
    webbrowser.open('https://thatsthem.com', new=2)
    webbrowser.open('https://www.spokeo.com/email-search', new=2)
if(option == "4"):
    option = input("[+]Enter phone number: ")
    webbrowser.open("http://demo.phoneinfoga.crvx.fr/api/numbers/"+ option +"/scan/local", new=2)
    webbrowser.open("http://demo.phoneinfoga.crvx.fr/api/numbers/"+ option +"/scan/googlesearch", new=2)
    webbrowser.open('https://www.411.com/reverse-phone', new=2)
    webbrowser.open('https://www.spokeo.com/reverse-phone-lookup', new=2)
    webbrowser.open("https://freecarrierlookup.com/", new=2)
    webbrowser.open("http://fonefinder.net/", new=2)
    webbrowser.open('https://www.intelius.com/', new=2)
if (option == "5"):
    webbrowser.open('https://www.411.com/reverse-address', new=2)
    webbrowser.open('https://www.spokeo.com/reverse-address-search', new=2)
    webbrowser.open('https://www.intelius.com/', new=2)
    webbrowser.open("https://www.peoplefinder.com/", new=2)
if (option == "6"):
    webbrowser.open("https://pimeyes.com/en", new=2)
    webbrowser.open("https://tineye.com/", new=2)
    webbrowser.open("https://exifdata.com/", new=2)
if (option == "7"):
    webbrowser.open('https://www.macvendorlookup.com/', new=2) 
if (option == "8"):
    webbrowser.open('https://search.censys.io/', new=2)
    webbrowser.open('https://www.robtex.com/', new=2) 
    webbrowser.open('https://who.is', new=2) 
    webbrowser.open('https://lookup.icann.org/en', new=2)     
    webbrowser.open('https://check-host.net/?lang=en', new=2)
if (option == "9"):
    webbrowser.open('https://skidsearch.net/panel/login.php', new=2) 
    webbrowser.open('https://leakix.net/', new=2) 
    webbrowser.open('https://intelx.io/tools?tab=general', new=2)     
    webbrowser.open('https://check-host.net/?lang=en', new=2)    
    webbrowser.open('https://haveibeenpwned.com/', new=2)  
    webbrowser.open('https://doxbin.net/', new=2)
    webbrowser.open('https://skidbin.net/', new=2)
    webbrowser.open('https://breached.co/Announcement-Database-Index', new=2)