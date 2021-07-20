from random import randint
import time
import os

#---- Обозначения на доске!
#+ : корабь
#X : корабь убит
#O : мимо

class Board(object):
	def __init__(self):
		self.DefaultSettings()
		self.GameInit()
	def DefaultSettings(self): #Loading default settings 
		self.board = []
		self.enemy_board = []
		self.fake_board = []
		self.ships = []
		self.enemy_ships = []
		self.Player_win = 0
		self.Bot_win = 0
		self.width = 10
		self.height = 10
		self.system = 0
		self.IncorrectCoords = 0

	def GameInit(self): #Initializing game processes
		self.StartGame_message() #Information in start
		os.system('cls')
		self.get_prop() #Taking game_board proportions
		self.GenerateBoard() #Filling the board based on proportions
		self.FillBoard() #Generating ships positions
		time.sleep(1)
		if self.system == 0: #system_mode activation
			self.GameLoop() #Loading main game process
		else:
			self.ShowBoard(0)
			os.system('cls')
			self.GameLoop()

	def GameLoop(self):
		while self.Player_win == self.Bot_win:
			self.IncorrectCoords = 0
			while self.IncorrectCoords == 0:
				os.system('cls')
				self.ShowBoard(0)
				self.ShowBoard(1)
				try:
					x,y = self.xy() #Taking attacked cell from coordinates from player
				except TypeError:
					break
				self.CheckCell(x,y) #Checking played attacked cell
			#Ход Бота
			self.IncorrectCoords = 0
			while self.IncorrectCoords == 0:
				x,y = self.getCoords() #Taking attacked cell from coordinates from bot
				self.CheckBotCell(x,y) #Checking played attacked cell from bot
			#Проверка Кораблей
			os.system('cls')
			self.DetectAviableShips() #Checking win_status

	def DetectAviableShips(self):
		if len(self.ships) == 0:
			self.Player_win = 1
			os.system('cls')
			print("Вы проиграли!")
		elif len(self.enemy_ships) == 0:
			self.Bot_win = 1
			os.system('cls')
			print("Вы победили!")

	def CheckCell( self, x, y ):
		if self.enemy_board[y][x] == '+':
			self.enemy_board[y][x] = 'X'
			self.fake_board[y][x] = 'X'
			print("Корабль подбит")
			self.DelShip(0,x,y)
			time.sleep(0.3)
		elif self.enemy_board[y][x] == '0':
			print("Вы сюда уже стреляли!")
			time.sleep(0.3)
		elif self.enemy_board[y][x] == 'X':
			print("Этот корабль уже подбит")
			time.sleep(0.3)
		elif self.enemy_board[y][x] == ' ':
			self.enemy_board[y][x] = '0'
			self.fake_board[y][x] = '0'
			print("Мимо!")
			time.sleep(0.3)
			self.IncorrectCoords = 1

	def CheckBotCell( self, x, y ):
		if self.board[y][x] == '+':
			self.board[y][x] = 'X'
			print("Бот: попадание!")
			self.DelShip(1,x,y)
			time.sleep(0.3)
		elif self.board[y][x] == ' ':
			self.board[y][x] = '0'
			print("Бот: мимо!")
			self.IncorrectCoords = 1
			time.sleep(0.3)
		else:
			pass
	def ShowBoard( self, number ):
		if number == 0:
			br = self.board
			for k in br:
				print(" ".join(k))
			for a in range( 0, len(self.board[0]) ):
				print("_ ",end="")
			print("\n")
		else:
			for a in self.fake_board:
				print(" ".join(a))
			for a in range(0,len(self.fake_board)):
				print("_ ",end="")
			print("\n")
			

	def GenerateBoard(self):
		for a in range( 0, self.height ):
			self.board.append( [" "]*self.width )
			self.enemy_board.append( [" "]*self.width )
			self.fake_board.append( [" "]*self.width )

	def FillBoard(self):
		for a in range(0,2):
			x = randint(0,len(self.board)-1)
			y = randint(0,len(self.board[0])-1)
			if a == 1:
				self.ships.append((x,y))
			else:
				self.enemy_ships.append((x,y))
		for a in range(0,5):
			while 1:
				x = randint(0,len(self.board))
				y = randint(0,len(self.board[0]))
				cdrs = (x,y)
				acpt = self.CheckShipPos(cdrs,0)
				if acpt == 1:
					cdrs = ((cdrs[0]-1),(cdrs[1]-1))
					self.ships.append(cdrs)
					break
			while 1:
				x = randint(0,len(self.board))
				y = randint(0,len(self.board[0]))
				cdrs = (x,y)
				acpt = self.CheckShipPos(cdrs,1)
				if acpt == 1:
					cdrs = ((cdrs[0]-1),(cdrs[1]-1))
					self.enemy_ships.append(cdrs)
					break
		for a in self.ships:
			self.board[a[1]][a[0]] = '+'
		for a in self.enemy_ships:
			self.enemy_board[a[1]][a[0]] = '+'

	def xy(self):
		while 1:
			try:
				x = int(input("Введите X: "))-1
				if x < 0 or x > len(self.board[0])-1:
					list.append()
				y = int(input("Введите Y:"))-1
				if y < 0 or y > len(self.board)-1:
					list.append()
				return x,y
				self.IncorrectCoords = 1
				break
			except KeyboardInterrupt:
				try:
					k = input("Вы хотите выйти? (y/n) |> ")
					k = str(k)
					if k == 'y':
						self.Bot_win = 1
						print("Вы вышли!")
						break
				except:
					print("Вы ввели не (y/n)!")
			except:
				print("Ошибка")

	def get_prop(self):
		while 1:
			if self.system == 1:
				break
			try:
				self.width = int( input( "Введите ширину: " ) )
				if self.width == 0 or self.width < 0:
					list.append()
				self.height = int( input( "Введите высоту: " ) )
				if self.height == 0 or self.height < 0 :
					list.append()
				break
			except KeyboardInterrupt:
				try:
					k = input("\n Вы хотите выйти? (y/n) |> ")
					k = str(k)
					if k == 'y':
						self.Bot_win = 1
						print("Вы вышли!")
						break
				except:
					print("Вы ввели не (y/n)!")
			except:
				print( "Ошибка!" )

	def getCoords(self):
		x = randint( 0, len(self.board[0])-1)
		y = randint( 0 ,len(self.board)-1)
		return x,y

	def DelShip( self, num, x, y ):
		if num == 0:
			self.enemy_ships.remove((x,y))
		else:
			self.ships.remove((x,y))

	def CheckShipPos( self, pos, num ):
		if num == 0:
			xk = self.ships
		else:
			xk = self.enemy_ships
		for a in xk:
			if pos[0] != a[0]:
				if pos[0] - a[0] == 1 or a[0] - pos[0] == 1:
					return 0
				elif pos[0] - a[0] > 1 or a[0] - pos[0] > 1:
					return 1
			else:
				if pos[1] != a[1]:
					if pos[1] - a[1] == 1 or a[1] - pos[1] == 1:
						return 0
					elif pos[1] - a[1] > 1 or a[1] - pos[1] > 1:
						return 1
				else:
					return 0


	def StartGame_message(self):
		print("Обозначения кораблей:")
		print("+ : корабль\n" + "0 : не попал\n" + "X : корабль убит")
		print("Приятной игры!")
		if self.system != 1:
			time.sleep(4.3)
Board()
