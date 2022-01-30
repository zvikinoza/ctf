import sys
import requests
from base64 import b64decode, b64encode
from tqdm import tqdm

def bit_flip(pos, bit, data):
    raw = b64decode(b64decode(data).decode())

    list1 = bytearray(raw)
    list1[pos] = list1[pos] ^ bit
    raw = bytes(list1)
    return b64encode(b64encode(raw)).decode()

if len(sys.argv) != 2:
    print('try: python3 filename.py cipher_to_break')
    exit()
cookie = sys.argv[1].strip()

for position_idx in tqdm(range(60, len(cookie)), desc="Bruteforcing Position"):
    for bit_idx in tqdm(range(128), desc="Bruteforcing Bit"):
        auth_cookie = bit_flip(position_idx, bit_idx, cookie)
        cookies = {'auth_name': auth_cookie}
        r = requests.get('http://mercury.picoctf.net:15614/', cookies=cookies)
        if "picoCTF{" in r.text:
            print(r.text)
            break
