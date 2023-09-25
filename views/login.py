from flet import *
from connectdb import conn



class Login(UserControl):
	def __init__(self):
		super().__init__()
		self.username = TextField(label="username")
		self.password = TextField(label="password")

	def login_user(self,e):
		us_input = self.username.value
		pw_input = self.password.value

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM login where username=? AND password=?",(us_input,pw_input))
		user_data = cursor.fetchone()

		if user_data:
			print("you found user")
			print(user_data)
			self.page.client_storage.set("loginkey",user_data[1])
			# AND REDIRECT
			self.page.go("/")
		else:
			print(" no use found")

		self.update()


	def build(self):
		return Column([
			Text("Login",size=20),
			self.username,
			self.password,
			ElevatedButton("login",
				bgcolor="blue",color="white",
				on_click=self.login_user
				),
			ElevatedButton("register",
				bgcolor="orange",color="white",
				on_click=lambda _:self.page.go("/register")
				),
			ElevatedButton("Forgot avcount",
				bgcolor="green",color="white",
				on_click=lambda _:self.page.go("/forgot")
				),
			# AND FORCE DASHBOARD IF NOT LOGIN
			ElevatedButton("Force to dashboard",
				bgcolor="red",color="white",
				on_click=lambda _:self.page.go("/")
				),

			])
