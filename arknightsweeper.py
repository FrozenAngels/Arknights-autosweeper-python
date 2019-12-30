#Arknights automatic sweeping script.
#Warning:0/120 consciousness will be remain.
import os
import time
from configparser import ConfigParser
def click(x,y):
	os.system('adb shell input {} {}'.format(x,y))
	print('clicked specfic button @ ({},{})'.format(x,y))

print('One device adb_based automatic script for Arknights sweeping')
conf = ConfigParser()
if os.path.exists('config.ini') == False:
	print('Config files not exist,now generating...')
	#key button setting
	file=open('config.ini','w')
	Startkeyx=input('start key x:')
	Startkeyy=input('Start key y:')
	actionkeyx= input('action key x:')
	actionkeyy= input('action key y:')
	conf.add_section('buttons')
	conf.set('buttons','startkeyx',Startkeyx)
	conf.set('buttons','actionkeyx',actionkeyx)
	conf.set('buttons','startkeyy',Startkeyy)
	conf.set('buttons','actionkeyy',actionkeyy)
	conf.write(file)
	file.close()
	print('Configuration complete...')
	startx=int(Startkeyx)
	starty=int(Startkeyy)
	actionx=int(actionkeyx)
	actiony=int(actionkeyy)
else:
	config=conf.read('config.ini')
	startx=int(conf.get('buttons','startkeyx'))
	actionx=int(conf.get('buttons','actionkeyy'))
	starty=int(conf.get('buttons','startkeyy'))
	actiony=int(conf.get('buttons','actionkeyy'))
	print('Got existing config...')
#System mininum requirements checking...
if os.system('adb devices')!=0:
	print('Checking ADB daemon Failed!\nMake sure adb platform is properly configured on your System!')
	print('Program exited with code 2')
	exit(2)
else:
	while True:
		elapse=(input('Target sweeping time(seconds): '))
		try:
			elapse=int(elapse)
		except ValueError as noinput:
			print('Invaild Input\n')
			continue
		else:
			print('time set as {}s'.format(elapse))
			break

	while True:
		cnt=(input('Target sweeping counts(interger): '))
		try:
			cnt=int(cnt)
		except ValueError as noinput:
			print('Invaild Input\n')
			continue
		else:
			print('counts set as {} times'.format(cnt))
			if cnt >=6:
				print('Warning , a large number of storysweeping requests has been detected.\nPlease be aware of character consciousness remaining.\n')
			break
uselessvariable=input("Connect your device to the computer.\nMake sure there is only ONE device connected!\nPress Enter key if you are ready...")
print('Start sweeping...')
os.system('adb shell input tap {} {}'.format(actionx,actiony))
while cnt > 0 :
	print('{}times left'.format(cnt))	
	time.sleep(3)
	os.system('adb shell input tap {} {}'.format(startx,starty))
	time.sleep(1)
	os.system('adb shell input tap {} {}'.format(startx-100,starty-150))
	time.sleep(elapse+5)
	os.system('adb shell input tap {} {}'.format(233,233))
	time.sleep(8)
	cnt-=1
print('Selected sweeping process Completed.Program will be exited.')


