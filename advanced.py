import argparse
from langdetect import detect_langs
from langdetect import detect

test_string = '''
P aopur aol hjjlwalk huzdly pz nylha, iba dof kvu'a fvb kv pa lewspjpasf?'''

def is_english(string):
    res = detect_langs(string)
    
    if res[0].lang == 'en':
        return True
    else:
        return False

def caesar_cipher(message, key):
    if key>26:
        key = key % 26
    key = -key

    output = ''

    for i in message:
        if i.isalpha():
            num = ord(i)
            num+=key

            if i.isupper():
                if num > ord('Z'):
                    num = num - 26
                elif num < ord('A'):
                    num = num + 26
            elif i.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num + 26
            output += chr(num)
        else:
            output += i

    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to be opened')
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file_obj:
            string = file_obj.read()
    except:
        print('File not found.')
    
    possible_keys = []

    for i in range(1,26):
        nstr = caesar_cipher(string,i)
        
        if is_english(nstr):
            possible_keys.append(i)

    en_prob = []
    for i in possible_keys:
        res = detect_langs(caesar_cipher(string,i))
        
        if res[0].lang == 'en':
            en_prob.append(res[0])

    possible_key = possible_keys[en_prob.index(max(en_prob))]

    print(caesar_cipher(string,possible_key))

if __name__ == '__main__':
    main()























