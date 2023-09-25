from flet import *
from views.dashboard import Dashboard
from views.login import Login
from views.register import Register
from views.forgot import Forgot



def main(page:Page):
	page.window_width = 300

	# AND CHECK YOU SESSION HAVE OR NOT
	def check_session():
		session = page.client_storage.get("loginkey")
		print(f"check login session : {session}")
		return session


	# AND NOW I WILL DEFINE ROUTE
	def myroute(route):
		page.views.clear()
		page.views.append(
			View(
				"/",[
					Dashboard() if not check_session() == None else Column([
						Text("Sorry you must login"),
						ElevatedButton("login",
							on_click=lambda _:page.go("/login")
							)
						])
				]
				)
			)
		if page.route == "/login":
			page.views.append(
				View(
					"/login",[
						Login()
					]
					)

				)
		elif page.route == "/register":
			page.views.append(
				View(
					"/register",[
						Register()
					]
					)

				)
		elif page.route == "/forgot":
			page.views.append(
				View(
					"/forgot",[
						Forgot()
					]
					)

				)
	page.on_route_change = myroute
	page.go(page.route)


flet.app(target=main)
