import socket, string
from databaseControl import *
from random import randint
from time import *
from multiprocessing import Pool
 
plik = open("pasy.txt", "r")

# Set all the variables necessary to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = "botherrington"
PORT = 6667
PASS = plik.read()
readbuffer = ""
MODT = False
 
# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #yarakii \r\n")

db = databaseControl()	
 
# Method for sending a message
def Send_message(message):
    s.send("PRIVMSG #yarakii :" + message + "\r\n")

def getUserPoints(user, db):
	points = db.getUserPoints(user)
	print points
	return points

def roulette(user, points):
	points = int(points)
	userPoints = int(db.getUserPoints(user))
	print userPoints
	print points
	if userPoints >= points:
		rand = randint(0,99)
		if rand>20:
			db.addPointsToUser(user, points)
			return user + " wygral wlasnie " + str(points) + "pktow FeelsGoodMan"
		else:
			db.addPointsToUser(user, points*-1)
			return user + " przegral wlasnie " + str(points) + "pktow FeelsBadMan"
	else:
		return user + " nie ma wystarczajaco punktow FeelsBadMan"
	
while True:
	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()
	for line in temp:
		print "Wiadomosc z serwera: " + line
	    # Checks whether the message is PING because its a method of Twitch to check if you're afk
		if (line[0] == "PING"):
			s.send("PONG %s\r\n" % line[1])
		else:
	        # Splits the given string so we can work with it better
			parts = string.split(line, ":") 
			if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
				try:
					# Sets the message variable to the actual message sent
					message = parts[2][:len(parts[2]) - 1]
				except:
					message = ""
	            # Sets the username variable to the actual username
				usernamesplit = string.split(parts[1], "!")
				username = usernamesplit[0]
	           
	            # Only works after twitch is done announcing stuff (MODT = Message of the day)
				if MODT:
					print username + ": " + message
					command = string.split(message, " ")
	                # You can add all your plain commands here
					if message == "!points":
						points = getUserPoints(username, db)
						message = ""
						message = username + " points = " + str(points)
						Send_message(message)
						print "wysylam wiadomosc " + message
					if command[0] == "!roulette":
						Send_message(roulette(username, command[1]))
 
				for l in parts:
					if "End of /NAMES list" in l:
						MODT = True
	sleep(1 / 20/float(30))






