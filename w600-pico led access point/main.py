# based mainly on https://www.youtube.com/watch?v=GVMuER7A770
#inspired from https://maker.pro/forums/threads/w600-pico-webserver.292684/


from machine import Pin
import easyw600,w600

#create access point
easyw600.createap(ssid="W600_softAP") 
#create ftp server ( can be manipulate with dos ftp or the free ftp https://filezilla-project.org/
w600.run_ftpserver(port=21,username="user",password="12345678") 

# setup the webserver
try:
    import usocket as socket
except:
    import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket, address family type = AF_INET, socket type = SOCK_STREAM
s.bind(('', 80))
s.listen(5) # accept connections. backlog = 5 = max. number of unaccepted connections before refusing new connections

# interact with the hardware
led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
led_off = 1 # inverted logic
led_on = 0

# web page data
def web_page():
    file = open("index.html", "r")
    page = file.read()
    file.close()
    return page


# this is the main loop to handle requests
while True:
    conn, addr = s.accept() # accept connection with a new socket object "conn" to remote address "addr"
    request = conn.recv(1024) # receive from connected socket "conn" using 1024 byte buffer
    print(request) # for debugging only
    if "GET /?led=on" in request:
        led.value(led_on)
    if "GET /?led=off" in request:
        led.value(led_off)
      
#    led_status = ("ON", "OFF") led.value() ==1 # this should be valid python code, too, but I prefer the better readable form below.
    if led.value == 1: # same as before but imho better readable
        led_status = "ON"
    else:
        led_status = "OFF"
    response = web_page() % led_status # insert the actual status into the web page
    print(response) # debug
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text /html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()
