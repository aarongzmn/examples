import pglet
from pglet import Text, Textbox, Button, Checkbox

def main(page):
    
    logged_user = Text(f"Welcome, {page.user_login}!")

    def signout_clicked(e):
        page.signout()    

    def page_signin(e):
        print("Sign in event")
        logged_user.value = page.user_login
        page.update()

    def page_signout(e):
        logged_user.value = "Not logged in"
        page.update()

    page.on_signin = page_signin
    page.on_signout = page_signout

    page.add(
        logged_user,
        Button('Signout', on_click=signout_clicked)
    )

pglet.app("pglet-signin-test", target=main, local=False, permissions="*")