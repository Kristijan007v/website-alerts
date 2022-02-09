import yaml

with open("config.yaml", "r") as cf:
    try:
        config = yaml.safe_load(cf)
    except yaml.YAMLError as exc:
        print(exc)

#Saving email settings to variables
smtp = config["email"]["smtp"]
port = config["email"]["port"]
account = config["email"]["account"]
password = config["email"]["password"]
myemail = config["email"]["myemail"]
testEmail = config["email"]["test-mail"]["email-address"]

#Advanced settings
checkTime = config["script-settings"]["check-time"]
urlFile = config["script-settings"]["url-file"]
timezone = config["script-settings"]["timezone"]
sendAlerts = config["script-settings"]["send-alerts"]
dev = config["script-settings"]["dev"]

if dev == 'yes':
    print(testEmail)
    print("Config file is loaded successfully...")


