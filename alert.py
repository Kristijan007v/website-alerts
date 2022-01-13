import requests
import sendmail
import time
from requests.exceptions import ConnectionError
from datetime import datetime, timezone

now = datetime.now(tz = timezone.utc)
checkTime = 180 #Minimum check time needs to be set to 60 and needs to be whole number
checkMinutes = checkTime / 60
stringCheckTime = str(checkMinutes)
urlFile = 'urls.txt'
domainFile = 'domains.txt'

def Alert():
    while(True):
        print("-------------------------------------------------------------------------")
        print(now.strftime('%a %b %d %Z %Y'))
        print("-------------------------------------------------------------------------")
        with open(urlFile) as uFile:
            for url in uFile:
                checkUrl = url.strip()
                domain = checkUrl.replace("https://","")
                # For Python3, use print(line)
                if 'str' in url:
                    break
                try:
                    request = requests.get(checkUrl)
                except ConnectionError:
                    print()
                    print(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                    print('Website "' + url + '" is down!!!')
                    subject_alert = "Website alert - " + domain
                    message_alert = "Website " + url + " is down!"
                    sendmail.send_alert(subject_alert, message_alert, 'work@kristijan.me')
                else:
                    request = requests.get(checkUrl)
                    if request.status_code == 200:
                        print()
                        print(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                        print('Website "'  + checkUrl + '" is up and running (STATUS CODE:200)')
                    else:
                        print()
                        print(now.strftime('%a %b %d %H:%M:%S %Z %Y'))
                        print('Website "' + url + 'returned response code: {code}'.format(code=request.status_code))
                        subject_alert = "Website alert - " + domain
                        message_alert = 'Website "' + url + 'returned response code: {code}'.format(code=request.status_code)
                        sendmail.send_alert(subject_alert, message_alert, 'work@kristijan.me')
        print("Waiting " + stringCheckTime +  " minutes to check again...")
        time.sleep(checkTime)

Alert()        
    
