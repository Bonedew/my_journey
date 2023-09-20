import random
import time
import string

def welcome_message():
    print("Parooli generaator.")
    time.sleep(2)
    print("Arendaja: Ruuben Jalasto")

welcome_message()
time.sleep(2)
pw_length = int(input("Kui pikk peab parool olema?(1-15)"))
pw = ""
time.sleep(2)   
if pw_length >= 0 and pw_length <= 15:
    for i in range(int(pw_length)):
        if random.randint(0,1) == 1:
            pw += (random.choice(string.ascii_letters))
        else:
            pw += str((random.randint(0,9)))  
else:
    print("ERROR")
time.sleep(2)
print("Siin on su uus parool: " + pw)

