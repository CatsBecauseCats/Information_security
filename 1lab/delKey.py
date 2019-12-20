import os
key = "access.key"

if os.path.exists(key):
    os.remove(key)
else:
    print("The key does not exist!")

