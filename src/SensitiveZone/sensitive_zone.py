import os
from sqlite3 import connect
from typing import List, Tuple, Union
from contextlib import contextmanager

"""
Users Table
--------------------------------------------
ID  | Username | Student | Faculty | Trust |
++++++++++++++++++++++++++++++++++++++++++++
int | text     | bool    | bool    | text  |
--------------------------------------------

Authorization Table
-------------------------
ID  | Trust | Privilege |
+++++++++++++++++++++++++
int | text  | text      |
-------------------------
"""

class College:
	"""
	The moodule defines the data we want to protect against injection attacks.
	"""
	college = "./db/college.db"

	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()

	@contextmanager
	def users(self, curr) -> None:
		curr.execute("create table if not exists users(ID integer PRIMARY KEY, Username text, Student text, Faculty text, Trust text)")
		try:
			yield
		finally:
			pass
	
	@contextmanager
	def authorization(self, curr) -> None:
		curr.execute("create table if not exists authorization(ID integer PRIMARY KEY, Trust text, Privilege text)")
		try:
			yield
		finally:
			pass
	
	def get_data(self) -> Tuple[List]:
		return ["User1", "User2"], [True, False], [False, True],  ["T1", "T2"], ["View Grades", "Enter Grades"]
	
	def create(self):
		pass

class User(College):
	def __init__(self) -> None:
		super().__init__()

	def __str__(self) -> str: 
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
	
	def create(self):
		if os.path.exists(self.college):
			raise ValueError(f"{self.college} already exist!")
		else:
			with connect(self.college) as conn:
				curr = conn.cursor()
				with self.users(curr):
					username, student, faculty, trust, _ = self.get_data()
					for username, student, faculty, trust in zip(username, student, faculty, trust):
						curr.execute("INSERT into users(Username, Student, Faculty, Trust) VALUES(?, ?, ?, ?)", (username, student, faculty, trust))
					for row in curr.execute("SELECT * FROM users"): 
						print(row)
					print("Users table created")

class Authorization(College):
	def __init__(self) -> None:
		super().__init__()

	def __str__(self) -> str: 
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
	
	def create(self):
		with connect(self.college) as conn:
			curr = conn.cursor()
			with self.authorization(curr):
				_, _, _, trust, privilege = self.get_data()
				for trust, privilege in zip(trust, privilege):
					curr.execute("INSERT INTO authorization(Trust, Privilege) VALUES(?, ?)", (trust, privilege))
				for row in curr.execute("SELECT * from authorization"): 
					print(row)
				print("Authorization table created")

class DBManager(College):
	def __init__(self) -> None:
		super().__init__()

	def __str__(self) -> str: 
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
	
	def create(self):
		pass

	def query(self) -> List[Tuple]:
		with connect(self.college) as conn:
			for row in conn.cursor().execute("SELECT users.Username, authorization.Privilege FROM users, authorization WHERE users.Trust = authorization.Trust"):
				print(row)

	def display(self, table) -> List[Tuple]:
		with connect(self.college) as conn:
			for row in conn.cursor().execute(f"SELECT * FROM {table}"):
				print(row)

	def has_entergrades_secure(self, username) -> bool:
		with connect(self.college) as conn:
			cur = conn.cursor()
			cur.execute("SELECT Trust FROM users WHERE username = ?", (username,))
			trust_level = cur.fetchone()
		if trust_level is None:
			return ValueError("User doesn't exist!").__repr__()
		return True if trust_level[0] == "T2" else False

	def has_entergrades_secure1(self, username) -> Union[None, bool]:
		with connect(self.college) as conn:
			cur = conn.cursor()
			cur.execute("SELECT Trust FROM users WHERE username = ?", (username,))
			trust_level = cur.fetchone()
		if trust_level is None:
			return
		return True if trust_level[0] == "T2" else False