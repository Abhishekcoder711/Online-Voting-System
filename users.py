import getpass

class User:
	users_db={}
	def __init__(self, username, password):
		self.username = username
		self.password=password
		self.has_voted=False
	@classmethod
	def add_user(cls, username, password):
		if username in cls.users_db:
			print("Username already exits. Please try a different username.")
			return False
		cls.users_db[username]=User(username,password)
		return True
	@classmethod
	def authenticate(cls, username, password):
		user = cls.users_db.get(username)
		if user and user.password == password:
			return user
		return None

def register_user():
	username = input("Enter a username: ")
	password = getpass.getpass("Enter a password: ")
	if User.add_user(username, password):
		print("User registered successfully.")
	else:
		print("Registration Failed.")

def login_user():
	username = input("Enter a username: ")
	password = getpass.getpass("Enter a password: ")
	user = User.authenticate(username,password)
	if user:
		print("Login successful.")
	else:
		print("Invalid username or password.")