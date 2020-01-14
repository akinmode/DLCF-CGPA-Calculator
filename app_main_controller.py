#Codes for Initialization ...
#Import default python libraries.
import webbrowser as web

#Import application libraries from core.
from app_model import Model
from app_views import Display

#Controller class for the application
class CummulativeGradePointAverage(object):
    def __init__(self):
        self.display = Display()
        #Initalize application in default web browser.
        #Use 127.0.0.1:3000 as Custom access for application
        url = "http://127.0.0.1:3000"
        web.open(url)

    def index(self):
        with open("views\/initial_form.html") as file_contents:
            dbase = Model()
            users = dbase.view_user()
            if users == []:
                contents = file_contents.read().rstrip("\n")
                output = self.display.page_open(), contents, self.display.page_close()
            else:
                only_user = dbase.view_user()[0]
                contents = "<h3 class='display-4 text-center'>Welcome back, %s </h3><br/><label class='text-center'>Click <a href='my_database'>My Database</a> to continue. <a href='edit_user_account/%s'>Edit User</a></label>" % (only_user[2], only_user[0])
                output = self.display.page_open(), str(contents), self.display.page_close()
            return output
    index.exposed = True

    def initialize_account(self, cgpa_number, cgpa_names, cgpa_email):
        #process Initialization form here
        #self.database.insert_into_user_account(int(cgpa_number), cgpa_names, cgpa_email)
        if cgpa_number == "" and cgpa_names == "" and cgpa_email == "":
            initialize_account_error = "Good"
        else:
            dbase = Model()
            user_account = dbase.insert_user(cgpa_number, cgpa_names, cgpa_email)
            contents = dbase.view_user()
            output = self.display.page_open(), contents, self.display.page_close()
            return output
    initialize_account.exposed = True

    def about(self):
        with open("views\/about_cgpa.html") as file_contents:
            contents = file_contents.read().rstrip("\n")
            output = self.display.page_open(), contents, self.display.page_close()
            return output
    about.exposed = True

    def my_database(self):
        with open("views\/my_database.html") as file_contents:
            dbase = Model()
            gcon = """
                Get there %s
            """ % "Good"
            content = dbase.view_user_database()
            contents = file_contents.read().rstrip("\n")
            output = self.display.page_open(), gcon, self.display.page_close()
            return output
    my_database.exposed = True

    def exit_application(self):
        #mainframe.engine.exit()
        close = ""
    exit_application.exposed = True
