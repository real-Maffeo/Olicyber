import subprocess
import re


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Path to the image file
image_path = "/home/sergio/Desktop/congratulations.png"

# Construct the command as a list of arguments
command = ["identify", "-verbose", image_path]

# Execute the command and capture the output
completed_process = subprocess.run(command, capture_output=True, text=True)

# Get the captured output
output = completed_process.stdout

# Print or manipulate the captured output as needed
print(output)

numbers = re.findall(r'\s-?\b\d+\b\s', output)

prime = []

for number in numbers:
    if is_prime(int(number)) and number not in prime:
        prime.append(number)
prime = prime[:3]
num = 1
for i in range (len(prime)): 
    prime[i] = int(prime[i].strip())
    num *= prime[i]

print(prime)
print(num)

text = '''{A KOAN}
A MAN DECIDED TO GO AND STUDY WITH A MASTER
HE WENT TO THE DOOR OF THE MASTER
"WHO ARE YOU WHO WISHES TO STUDY HERE" ASKED THE MASTER
THE STUDENT TOLD THE MASTER HIS NAME
"THAT IS NOT WHO YOU ARE, THAT IS ONLY WHAT YOU ARE CALLED
WHO ARE YOU WHO WISHES TO STUDY HERE" HE ASKED AGAIN
THE MAN THOUGHT FOR A MOMENT, AND REPLIED "I AM A PROFESSOR"
"THAT IS WHAT YOU DO, NOT WHO YOU ARE," REPLIED THE MASTER
"WHO ARE YOU WHO WISHES TO STUDY HERE"
CONFUSED, THE MAN THOUGHT SOME MORE
FINALLY, HE ANSWERED, "I AM A HUMAN BEING"
"THAT IS ONLY YOUR SPECIES, NOT WHO YOU ARE
WHO ARE YOU WHO WISHES TO STUDY HERE", ASKED THE MASTER AGAIN
AFTER A MOMENT OF THOUGHT, THE PROFESSOR REPLIED "I AM A CONSCIOUSNESS INHABITING AN ARBITRARY BODY"
"THAT IS MERELY WHAT YOU ARE, NOT WHO YOU ARE
WHO ARE YOU WHO WISHES TO STUDY HERE"
THE MAN WAS GETTING IRRITATED
"I AM," HE STARTED, BUT HE COULD NOT THINK OF ANYTHING ELSE TO SAY, SO HE TRAILED OFF
AFTER A LONG PAUSE THE MASTER REPLIED, "THEN YOU ARE WELCOME TO COME STUDY' '''

# Split the text into an array where each row is an element
text_array = text.split('\n')

# Remove empty lines
text_array = [line for line in text_array if line.strip()]

# Print the resulting array
for row in text_array:
    print(row)

indexes = [    
    9, 43,
    19, 50,
    5, 35,
    1, 1,
    14, 41,
    19, 10,
    12, 11,
    7, 44,
    5, 23,
    20, 11,
    6, 58,
    16, 22,
    20, 63,
    8, 12,
    17, 27,
    2, 34,
    9, 4,
    20, 34,
    19, 57,
    15, 35,
    8, 44,
    15, 80,
    18, 29,
    1, 8
]

flag = ""

print(indexes[9])

for i in range (0, len(indexes), 2):
    flag += text_array[indexes[i] - 1][indexes[i + 1] - 1] 

print(flag)