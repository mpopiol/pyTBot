import requests
import string
import sqlite3
from bs4 import BeautifulSoup

page = requests.get("https://tmi.twitch.tv/group/user/erroreq/chatters")
page = page.content
lines = string.split(page, "\n")

"""control = 0
for item in lines:
	if control == 0 and item.find("chatters")!=-1:
		control = 1
		print "Zaczynamy"
	elif control == 1 and "[" not in item and "]" not in item and "{" not in item and "}" not in item:
		nick = ""
		for i in item:
			tmp = ord(i)	
			if (tmp>96 and tmp<123) or (tmp>48 and tmp<58):
				nick+=i
		if nick == "erroreq":
			print nick
			exit()
		print nick"""

db = sqlite3.connect("sqlite.db")
cursor = db.cursor()
cursor.execute('SELECT POINTS FROM POINTS WHERE NICK = \'test\'')
print cursor.fetchone()
