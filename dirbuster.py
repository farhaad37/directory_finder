import requests

a = open("/usr/share/wordlists/dirb/common.txt", 'r')

url = input("enter the full url :- ")

print("process on going....")

try:
    for item in a:
        r = requests.get(url+item)
        if r == 200:
            print(url+item+"     200OK")
        elif r == 403:
            print(url+item+"     403 access denied")
        elif r ==301:
            print(url+item+"     301")
        else:
            print("no")
except Exception as e:
    print(e)