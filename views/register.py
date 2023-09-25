from flet import *
from connectdb import conn
class Register(UserControl):
	def __init__(self):
		super().__init__()
		self.username = TextField(label="username")
		self.password = TextField(label="password")

	def add_register(self,e):
		us_input = self.username.value
		pw_input = self.password.value

		cursor = conn.cursor()
		cursor.execute('''
			INSERT INTO login (username,password)
			VALUES(?,?)

			''',(us_input,pw_input))
		conn.commit()
		print(f"you success add user {us_input}")
		

	def build(self):
		return Column([
			Text("register",size=20),
			self.username,
			self.password,
			ElevatedButton("register",
				on_click=self.add_register
				),
			# AND FOR LOGIN REDIRECT
			ElevatedButton("login",
				on_click=lambda _:self.page.go("/login")
				),
			])
