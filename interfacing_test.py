import serial
# from tools.ccTalk import *
from ccTools.ccTalk import *
import time
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

print(ser)


def sendMessage(header, data='', source=1, destination=2):
    request = ccTalkMessage(header=header, payload=data, source=source, destination=destination)
    print " -> " + str(request)
    ser.write(request.raw())

    # print request
    time.sleep(0.01)
    data = ser.read(20)
    # print (data)
    messages = parseMessages(data)[1]
    print messages
    print " <- " + str(messages[1])
    print("Data: %s\n" % messages[1].payload.data)
    return messages[1]

print "[*] Pinging device..."

ok = False

# Wait for device to be initiated
while not ok:
    try:
        response = sendMessage(249)
    except:
        continue
    if response.payload.header == 0:
        ok = True
    else:
        print response.payload.header

# print "[*] Request manufacturer id ..."
sendMessage(239,  '\x15')
# sendMessage(1)
