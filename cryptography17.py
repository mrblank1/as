from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
from cryptography.hazmat.backends import default_backend
import os
preshared_key=bytes.fromhex('00112233445566778899AABBCCDDEEFF')
preshared_iv = bytes.fromhex('00000000000000000000000000000000')
aesContext=Cipher(algorithms.AES(preshared_key), modes.CTR(preshared_iv),backend=default_backend())
message= b"""
<XML>
<CreditCardPurchase>
<Merchant>Acme Inc</Merchant>
<Buyer>John Smith</Buyer>
<Date>01/01/2001</Date>
<Amount>$100.00</Amount>
<CCNumber>555-555-555-555</CCNumber
</CreditCardPurchase>
</XML>   """
encryptor=aesContext.encryptor()
ciphertext=encryptor.update(message)
print(ciphertext)