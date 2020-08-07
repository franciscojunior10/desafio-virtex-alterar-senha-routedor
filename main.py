import telnetlib

HOST = "192.168.0.1"
PORT = 23

user = input("Enter your remote account: ")
password = input("Enter with password: ")
new_password = input("Enter new password: ")

tn = telnetlib.Telnet(HOST,PORT)

tn.read_until(b"username:")
tn.write(user.encode() + b"\r")

tn.write(user.encode('ascii') + b"\n")
print('Login successfully')

tn.read_until(b"password:")
tn.write(password.encode() + b"\r")

tn.read_until(b"TP-LINK(conf)#")

cmd = ("wlctl set --sec psk wpa2 auto " + new_password + "\r").encode() 
tn.write(cmd)

tn.read_until(b"[ rsl_sendAppWlanCfg ] 882:  Tell TMPD server that wlan/guest cfg has been changed.")

tn.read_until(b"cmd:SUCC")

tn.write(b"exit\r")

print('Password changed successfully')