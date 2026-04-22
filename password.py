import random
import string
def generate_password():
    print("\n --- Password Generator ---")
    length = int(input("Enter the desired password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password: ", password)
