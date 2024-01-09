# ----------Creating a key start----------
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("mykey.key", "wb") as mykey:
    mykey.write(key)
# ----------Creating a key end----------

# ----------Loading a key start----------
with open("mykey.key", "rb") as mykey:
    key = mykey.read()
print(key)
# ----------Loading a key end----------

# ----------encryption stat----------
f = Fernet(key)

with open("Mall_Customers.csv", "rb") as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open("enc_Mall_Customers.csv", "wb") as encrypted_file:
    encrypted_file.write(encrypted)
# ----------encryption end----------


# ----------decryption start----------
f = Fernet(key)

with open("enc_Mall_Customers.csv", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open("dec_Mall_Customers.csv", "wb") as decrypted_file:
    decrypted_file.write(decrypted)
# ----------decryption end----------
