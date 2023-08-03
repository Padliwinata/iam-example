import time
import pyotp
import qrcode
  
key = "secret"
  
uri = pyotp.totp.TOTP(key).provisioning_uri(
    name='Rama_Padliwinata',
    issuer_name='IAMServer')
  
print(uri)
  
  
# Qr code generation step
qrcode.make(uri).save("qr_auth.png")
  
"""Verifying stage starts"""
  
totp = pyotp.TOTP(key)
  
# verifying the code
while True:
  print(totp.verify(input(("Enter the Code : "))))