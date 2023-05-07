Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.platform
'win32'
>>> 
>>> 
>>> print(sys.version)
3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)]
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()
'C:\\Users\\wdavi\\AppData\\Local\\Programs\\Python\\Python39'
>>> 
>>> 
>>> os.eviron
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.eviron
AttributeError: module 'os' has no attribute 'eviron'
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\wdavi\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'WD-LENOVO', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOME': 'C:\\Users\\wdavi', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\wdavi', 'LOCALAPPDATA': 'C:\\Users\\wdavi\\AppData\\Local', 'LOGONSERVER': '\\\\WD-LENOVO', 'NUMBER_OF_PROCESSORS': '2', 'ONEDRIVE': 'C:\\Users\\wdavi\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Users\\wdavi\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\wdavi\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\wdavi\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Users\\wdavi\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 21 Model 112 Stepping 0, AuthenticAMD', 'PROCESSOR_LEVEL': '21', 'PROCESSOR_REVISION': '7000', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\wdavi\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\wdavi\\AppData\\Local\\Temp', 'USERDOMAIN': 'WD-LENOVO', 'USERDOMAIN_ROAMINGPROFILE': 'WD-LENOVO', 'USERNAME': 'wdavi', 'USERPROFILE': 'C:\\Users\\wdavi', 'WINDIR': 'C:\\Windows'})
>>> 
>>> 
>>> 
>>> import datetime
>>> datetime.date.today()
datetime.date(2021, 11, 28)
>>> 
>>> 
>>> 
>>> datetime.date.today().day
28
>>> 
>>> datetime.date.today().month
11
>>> 
>>> 
>>> datetime.date.today().year
2021
>>> 
>>> 
>>> datetime.date.isoformat(datetime.date.today())
'2021-11-28'
>>> 
>>> 
>>> import time
>>> time.strftime("%H:%M")
'23:08'
>>> 
>>> 
>>> 
>>> time.strftime("%A %p")
'Sunday PM'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import html
>>> html.escape("This HTML fragment contains a <script>script</script> tag.")
'This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'
>>> 
>>> 
>>> html.unescape("I &hearts; Python's &lt;standard library&gt;.")
"I ♥ Python's <standard library>."
>>> 