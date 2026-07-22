import os
import hashlib

password = "admin123"

print(password)

os.system("dir")

hash = hashlib.md5(password.encode()).hexdigest()

print(hash)