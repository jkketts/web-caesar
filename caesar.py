def encrypt(text,rot):

    newStr = ""
    rot = rot % 26

    for i in text:
        if (ord(i) >= 97 and ord(i) <= 122):
            if (ord(i)+rot > 122):
                newStr += chr((ord(i)+rot) - 26)
            else:
                newStr += chr(ord(i)+rot)
        elif (ord(i) >= 65 and ord(i) <= 90):
            if (ord(i)+rot > 90):
                newStr += chr((ord(i)+rot) - 26)
            else:
                newStr += chr(ord(i)+rot)
        else:
            newStr += i
    return newStr

def main():
    text = input('Type a message:')
    rot = int(input('Rotate By:'))
    encrypt(text, rot)

if __name__ == "__main__":
    main()