import hashlib

password = "hello"

hash = hashlib.md5(password.encode()).hexdigest()

print(hash)