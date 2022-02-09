import settings
import sendmail
import requests
import time 
from requests.exceptions import ConnectionError
from datetime import datetime, timezone
from logger import log

checkTime = settings.checkTime #Minimum check time needs to be set to 60 and needs to be whole number
checkMinutes = checkTime / 60
stringCheckTime = str(checkMinutes)
urlFile = settings.urlFile
recipients_all = settings.myemail #Here goes your email from config.yaml

#You can also add multiple recipients
#Here are some of the examples
recipients_pozgaj = ['work@kristijan.me', 'kiki.vidovic.6969@gmail.com']
recipients_kindwhenhard = ['work@kristijan.me', 'kiki.vidovic.6969@gmail.com']
recipients_bdflogistics = 'work@kristijan.me'

def Alert():
    while(True):
        now = datetime.now(tz = timezone.utc)
        print("-------------------------------------------------------------------------")
        print(now.strftime('%a %b %d %Z %Y'))
        print("-------------------------------------------------------------------------")
        #Write logs
        log("-------------------------------------------------------------------------")
        log(now.strftime('%a %b %d %Z %Y'))
        log("-------------------------------------------------------------------------")
        with open(urlFile) as uFile:
            for url in uFile:
                checkUrl = url.strip()
                domain = checkUrl.replace("https://","")
                if 'str' in url:
                    break
                try:
                    request = requests.get(checkUrl)
                except ConnectionError:
                    print()
                    print(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                    print('Website "' + url + '" is down!!!')
                    #Write logs
                    log('\n')
                    log(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                    log('Website "' + url + '" is down!!!')
                    if(domain == "pozgaj.eu" or domain == "azelija.com" or domain == "agroturizam-pozgaj.com"):
                        #Send email alerts
                        subject_alert = "Website alert - " + domain
                        message_alert = "Website " + url + " is down!"
                        sendmail.send_alert(subject_alert, message_alert, recipients_pozgaj)
                    elif (domain == "kindwhenhard.com"):
                        #Send email alerts
                        subject_alert = "Website alert - " + domain
                        message_alert = "Website " + url + " is down!"
                        sendmail.send_alert(subject_alert, message_alert, recipients_kindwhenhard)
                    else:
                        #Send email alerts
                        subject_alert = "Website alert - " + domain
                        message_alert = "Website " + url + " is down!"
                        sendmail.send_alert(subject_alert, message_alert, recipients_all)
                else:
                    request = requests.get(checkUrl)
                    if request.status_code == 200:
                        print()
                        print(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                        print('Website "'  + checkUrl + '" is up and running (STATUS CODE:200)')
                        #Write logs
                        log('\n')
                        log(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                        log('Website "'  + checkUrl + '" is up and running (STATUS CODE:200)')
                    else:
                        print()
                        print(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                        print('Website "' + url + 'returned response code: {code}'.format(code=request.status_code))
                        #Write logs
                        log('\n')
                        log(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                        log('Website "' + url + 'returned response code: {code}'.format(code=request.status_code))
                        #Send email alerts
                        subject_alert = "Website alert - " + domain
                        message_alert = 'Website "' + url + 'returned response code: {code}'.format(code=request.status_code)
                        sendmail.send_alert(subject_alert, message_alert, 'work@kristijan.me')
        print("Waiting " + stringCheckTime +  " minutes to check again...")
        log("Waiting " + stringCheckTime +  " minutes to check again...")
        time.sleep(checkTime)

Alert()        
    
