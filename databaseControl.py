import sqlite3
import string

class databaseControl:
	
	def __init__(self):
		self.db = sqlite3.connect("sqlite.db")
		self.cursor = self.db.cursor()
	
	def getUserPoints(self, user):
		command = 'SELECT POINTS FROM POINTS WHERE NICK = \'' + user + '\';'
		self.cursor.execute(command)
		result = str(self.cursor.fetchone())
		if result == "None":
			return -1
		resultOnlyNumbers = ""
		for i in result:
			tmp = ord(str(i))	
			if tmp>47 and tmp<58:
				print resultOnlyNumbers	
				resultOnlyNumbers = resultOnlyNumbers + i
		print resultOnlyNumbers
		return resultOnlyNumbers

	def addUser(self, user):
		command = 'INSERT INTO POINTS VALUES (\'' + user + '\', 0);'
		self.cursor.execute(command)
		self.db.commit()

	def addPoints(self, user, points):
		command = 'UPDATE POINTS SET POINTS = ' + str(points) + ' WHERE NICK = \'' + user + '\';' 
		self.cursor.execute(command)
		self.db.commit()

	def addPointsToUser(self, user, points):
		if len(user)>2:
			userPoints = self.getUserPoints(user)
			print userPoints
			if userPoints == -1:
				self.addUser(user)
				print "dodano do bazy"
				userPoints = 0
			userPoints = int(userPoints)
			userPoints += points
			self.addPoints(user, userPoints)
			return "done"