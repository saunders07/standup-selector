import random
import keyboard
import time
import inflect

p = inflect.engine()

print('Welcome to Stand-up!')
time.sleep(2)

names    = input('Enter names of Attendees:\n').split(", ")
shuffled = random.sample(names, len(names))
last     = shuffled[-1]

print('List of attendees:', ', '.join(names))
time.sleep(1)

for x in shuffled:
    index = shuffled.index(x) + 1
    ordinal = p.ordinal(index)

    print(ordinal,'...')
    time.sleep(1)

    print(x)
    time.sleep(1)
    print("Press 'space' for next person...")
    keyboard.wait('space')

    if x == last:
        print("End of Stand-up!")
        time.sleep(1)
        print("Have a good day!")
        time.sleep(1)