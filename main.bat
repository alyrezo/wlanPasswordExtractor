@echo off
cls
echo.
echo.
@echo     d8888b.  .d8b.  .d8888. .d8888. db   d8b   db  .d88b.  d8888b. d8888b.      
@echo     88  `8D d8' `8b 88'  YP 88'  YP 88   I8I   88 .8P  Y8. 88  `8D 88  `8D      
@echo     88oodD' 88ooo88 `8bo.   `8bo.   88   I8I   88 88    88 88oobY' 88   88      
@echo     88~~~   88~~~88   `Y8b.   `Y8b. Y8   I8I   88 88    88 88`8b   88   88      
@echo     88      88   88 db   8D db   8D `8b d8'8b d8' `8b  d8' 88 `88. 88  .8D      
@echo     88      YP   YP `8888Y' `8888Y'  `8b8' `8d8'   `Y88P'  88   YD Y8888D'      
echo.                                                                                
echo.                                                                                
@echo     d88888b db    db d888888b d8888b.  .d8b.   .o88b. d888888b  .d88b.  d8888b. 
@echo     88'     `8b  d8' `~~88~~' 88  `8D d8' `8b d8P  Y8 `~~88~~' .8P  Y8. 88  `8D 
@echo     88ooooo  `8bd8'     88    88oobY' 88ooo88 8P         88    88    88 88oobY' 
@echo     88~~~~~  .dPYb.     88    88`8b   88~~~88 8b         88    88    88 88`8b   
@echo     88.     .8P  Y8.    88    88 `88. 88   88 Y8b  d8    88    `8b  d8' 88 `88. 
@echo     Y88888P YP    YP    YP    88   YD YP   YP  `Y88P'    YP     `Y88P'  88   YD 
echo.                                                                                
echo.                                                                                        
echo.                                                                       
@echo                  https://github.com/alyrezo/wlanPasswordExtractor        
echo.     
echo.                                                                
                                                                       
setlocal EnableDelayedExpansion
goto :main

:getKey
for /F "tokens=2 delims=: usebackq" %%B in (`netsh wlan show profiles %1 key^=clear ^| find "Key Content"`) do (
        set _clear_key=%%B
        set _clear_key=!_clear_key:~1!
)
goto :eof

:main
for /F "tokens=2 delims=:" %%A in ('netsh wlan show profiles ^| find "User Profile"') do (
    set _profile_name=%%A
    set _profile_name=!_profile_name:~1!
    set _clear_key=No password
    
    call :getKey !_profile_name!
    
    echo !_profile_name:~0! : !_clear_key:~0!
)
