import pyrebase
import gpiozero
import logging

logger = logging.getLogger('scope.name')

file_log_handler = logging.FileHandler('logfile.log')
logger.addHandler(file_log_handler)

stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

# nice output format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log_handler.setFormatter(formatter)
stderr_log_handler.setFormatter(formatter)

RELAY_PIN = 2
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

config = {
  "apiKey": "IzaSyBppGvdpSZGpQkc9w1M-kcv-MAV2_lDorg",
  "authDomain": "automation-33f54.firebaseapp.com",
  "databaseURL": "https://automation-33f54.firebaseio.com",
  "storageBucket": "automation-33f54.appspot.com"
}
 
firebase = pyrebase.initialize_app(config)
 
#auth = firebase.auth()

db = firebase.database()
#lightStatus = db.child("deviceControl").get()



def stream_handler(message):
    logger.info("Light Status : " + message["data"])
    lightStatus = message["data"]
    if lightStatus == "ON":
        relay.on()
    elif lightStatus == "OFF":
        relay.off()
        
        
        

lightStream = db.child("deviceControl").child("light").child("status").stream(stream_handler)