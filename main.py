import subprocess
banner = """

     d8888b.  .d8b.  .d8888. .d8888. db   d8b   db  .d88b.  d8888b. d8888b.      
     88  `8D d8' `8b 88'  YP 88'  YP 88   I8I   88 .8P  Y8. 88  `8D 88  `8D      
     88oodD' 88ooo88 `8bo.   `8bo.   88   I8I   88 88    88 88oobY' 88   88      
     88~~~   88~~~88   `Y8b.   `Y8b. Y8   I8I   88 88    88 88`8b   88   88      
     88      88   88 db   8D db   8D `8b d8'8b d8' `8b  d8' 88 `88. 88  .8D      
     88      YP   YP `8888Y' `8888Y'  `8b8' `8d8'   `Y88P'  88   YD Y8888D'      
                                                                                
                                                                                
     d88888b db    db d888888b d8888b.  .d8b.   .o88b. d888888b  .d88b.  d8888b. 
     88'     `8b  d8' `~~88~~' 88  `8D d8' `8b d8P  Y8 `~~88~~' .8P  Y8. 88  `8D 
     88ooooo  `8bd8'     88    88oobY' 88ooo88 8P         88    88    88 88oobY' 
     88~~~~~  .dPYb.     88    88`8b   88~~~88 8b         88    88    88 88`8b   
     88.     .8P  Y8.    88    88 `88. 88   88 Y8b  d8    88    `8b  d8' 88 `88. 
     Y88888P YP    YP    YP    88   YD YP   YP  `Y88P'    YP     `Y88P'  88   YD 
                                                                                
                                                                                        
                                                                       
                  https://github.com/alyrezo/wlanPasswordExtractor        
 


"""
print(banner)
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
