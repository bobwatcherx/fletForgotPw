from flet import *
from connectdb import conn


class Forgot(UserControl):
    def __init__(self):
        super().__init__()
        self.name = TextField(label="insert name")

        # AND ADD FOR CONTAINER CHANGE USER IF USER INPUT FOUND
        self.change_user = Container(
            padding=10,
            visible=False,
            content=Column([
                TextField(label="change password here"),
                ElevatedButton("change now",
                    bgcolor="blue",color="white",
                    on_click=self.reset_account
                    )

                ])
            )

    def reset_account(self,e):
        # AND RESET ACCOUNT
        us_input = self.name.value
        pw_input = self.change_user.content.controls[0].value

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM login WHERE username=?', (us_input,))
        
        user_data = cursor.fetchone()

        if user_data:
            # AND UPDATE TBL
            cursor.execute("UPDATE login set password = ? where username = ?",(pw_input,us_input))
            conn.commit()
            print(f"password succes change : {us_input}")
            # AND REDIRECT BACK TO LOGIN
            self.page.go("/login")
        else:
            print(f"user not found {us_input}")
        self.update()

    def process_forgot(self,e):
        # FIRST I WILL FOUND USERNAME YOU INPUT HAVE OR NOT
        us_input = self.name.value
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM login where username=?',(us_input,))
        user_data = cursor.fetchone()

        if user_data:
            print(f"username you found  :{us_input}")
            # AND SHOW Container CHANGE PASWORD}
            self.change_user.visible = True

        else:
            print(f"username you not found  :{us_input}")
            # AND SHOW Container CHANGE PASWORD}
            self.change_user.visible = False

        self.update()

    def build(self):
        return Column([
            Text("Forgot",size=20),
            self.name,
            ElevatedButton("reset password",
                on_click=self.process_forgot
                ),
            self.change_user


            ])
