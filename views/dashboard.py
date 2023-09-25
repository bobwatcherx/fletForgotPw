from flet import *

class Dashboard(UserControl):
	def __init__(self):
		super().__init__()


	def logout(self,e):
		# AND REMOVE SESSION LOGIN
		self.page.client_storage.remove("loginkey")
		self.page.views.clear()
		# AND REDIRECT BACK TO LOGIN
		self.page.go("/login")
		print(self.page.route)
		self.update()

	def build(self):
		return Column([
			Text("helo in dashboard",size=20),
			# AND LOGOUT BTN
			ElevatedButton("logout",
				bgcolor="red",color="white",
				on_click=self.logout
				)
			])
