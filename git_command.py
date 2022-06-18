import os
def dowland_witch_git():
    os.system("git fetch")
    os.system("git pull")
    save()

def save():
    file = open("text.txt")
    tab = file.readlines()
    last = tab[0].replace("\n", "")
    last = int(last)
    with open("text.txt", "w") as file:
        file.write(f"{last + 1}")

if __name__ == '__main__':
    dowland_witch_git()
