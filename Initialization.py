"""
Program Cummulative Grade Performance Assessment (CGPA)
Custom Deeper Life Campus Fellowship, Awo Centre
Team ICT Directorate, 2018

Outline:
A Database to store all the subjects per unit course
A Calculator to generate the CGPA based on the Database

Initial Inputs to Custom the application:
Student's Name
Student's Matric Number
Student's Department
Student's Faculty

Other Inputs for Input Form:
Subject Title
SUbject Short Code
Subject Allocated Units
Subject Score

"""

#Codes for Initialization ...
#Import default python libraries.
import os
import cherrypy as mainframe
import webbrowser as web

#Import application libraries from core.
from app_model import Model
from app_views import View
from app_grade_generator import GradeGenerator
from htmltable import HtmlTable

#Controller class for the application
class CummulativeGradePointAverage(object):
    url = "http://127.0.0.1:3000"
    database_folder = "database"

    def __init__(self):
        self.display = View()
        if not os.path.exists(self.database_folder):
            os.makedirs(self.database_folder)
        #Initalize application in default web browser.
        #Use 127.0.0.1:3000 as Custom access for application
        web.open(self.url)

    def index(self, cgpa_number = "", cgpa_names = "", cgpa_cat = "", delete = ""):
        dbase = Model()
        users = dbase.view_user()
        if users == []:
            if cgpa_number == "" and cgpa_names == "" and cgpa_cat == "":
                users = ""
                index_contents = self.display.index_form()
            else:
                dbase.insert_user(cgpa_number, cgpa_names, cgpa_cat)
                new_user = dbase.view_user()[0]
                index_contents = self.display.index_welcome(new_user[2], new_user[0])
        else:
            users = dbase.view_user()[0][2]
            if cgpa_number == "" and cgpa_names == "" and cgpa_cat == "" and delete == "":
                only_user = dbase.view_user()[0]
                index_contents = self.display.index_welcome(only_user[2], only_user[0])
            elif cgpa_number == "" and cgpa_names == "" and cgpa_cat == "" and delete != "":
                #DELETING COURSE
                dbase.delete_user(delete)
                index_contents = """
                <section class="col-sm-6 mt-2 mx-auto text-center">
                    <label><a href=\"index\" class=\"btn btn-info\">Activate Application</a></label>
                </section>
                """
        return self.display.page_open(), self.display.page_nav(users), index_contents, self.display.page_close()
    index.exposed = True

    def my_database(self, c_code = "", c_title = "", c_level = "", c_unit = "", c_score = "", edit = "", delete = "", option = ""):
        dbase = Model()
        grades = GradeGenerator()

        users = dbase.view_user()
        my_link = dbase.view_user()[0]
        if my_link[3] == "UG":
            user_cat = "Undergraduate"
        else:
            user_cat = "Postgraduate"

        dbase_content = dbase.view_user_database()

        if dbase_content == []:
            if c_code == "" and c_level == "" and c_unit == "" and c_score == "":
                all_contents = "<section class=\"mt-3\"><p class=\"text-center text-info\">Your Courses are not available yet for calculating your CGPA</p></section>"
            else:
                c_grade = grades.generate_4_points(c_score)
                dbase.insert_user_database(c_code, c_title, c_level, c_unit, c_score, c_grade)
                all_contents = "<section class=\"mt-3\"><p class=\"text-center text-success\">Your Database has been initialized. Click \"View Updated Courses\" to continue.</p></section>"
        elif dbase_content != []:

            dbase_general_summary = dbase.general_summary()[0]
            tcourses = dbase_general_summary[0]
            tunits = dbase_general_summary[1]
            tcgpa = round(dbase_general_summary[2]/tunits, 2)

            #BREAKDOWN
            dbase_breakdown_summary = dbase.breakdown_summary()
            if dbase_breakdown_summary == []:
                display_breakdown_summary = ""
            else:
                display_all_summary = []
                for eachsummary in dbase_breakdown_summary:
                    tgpa = round(eachsummary[3]/eachsummary[2], 2)
                    eachline = "<label><strong>"+str(eachsummary[0])+" Level</strong><br/> Courses <span><em>"+str(eachsummary[1])+"</em></span>, Total Units: <span><em>"+str(eachsummary[2])+"</em></span>, GPA: <span><em><strong>"+str(tgpa)+"</strong></em></span></label><br/>"
                    display_all_summary.append(eachline)

                display_breakdown_summary_inner = "".join(display_all_summary)
                display_breakdown_summary = """
    <label><strong><u>CATEGORY</u></strong></label>: %s<br/>
    <label><strong><u>BREAKDOWN</u></strong></label><br/>
    %s
                """ % (user_cat, display_breakdown_summary_inner)

                if my_link[3] == "UG":
                    designate = grades.grade_scale_4_points(tcgpa)
                else:
                    designate = grades.grade_scale_msc_points(tcgpa)

            go = HtmlTable()
            go.add_headers(["Course Code", "Course Title", "Course Level", "Course Unit", "Course Score", "Course Grade"])
            go.add_rows(dbase_content)
            all_table = go.show_table()

            if c_code == "" and c_level == "" and c_unit == "" and c_score == "" and edit == "" and delete == "" and option == "":
                all_contents = self.display.database_summary(display_breakdown_summary, tcourses, tunits, tcgpa, designate, all_table)
            elif c_code != "" and c_level != "" and c_unit != "" and c_score != "" and edit == "" and delete == "" and option == "":
                try:
                    c_grade = grades.generate_4_points(c_score)
                    dbase.insert_user_database(c_code, c_title, c_level, c_unit, c_score, c_grade)
                except Exception as e:
                    double_entry_error = """
                    <section class="text-center col-sm-8 mt-2 mx-auto">
                        <label class="text-danger">Double Entry Error: Your Database already has a course with the code %s</label><br/>
                        <labe><a href=\"my_database\" class=\"btn btn-info w-50\">Bact to my Database</a></label>
                    </section>
                    """ % (c_code)
                    all_contents = double_entry_error
                else:
                    all_contents = self.display.database_summary(display_breakdown_summary, tcourses, tunits, tcgpa, designate, all_table)
            elif c_code == "" and c_level == "" and c_unit == "" and c_score == "" and edit != "" and delete == "" and option == "off":
                one_course = dbase.select_user_course(edit)[0]
                edit_content = """<h3 class=\"display-5 d-inline-block w-75\"><i class="fas fa-edit"></i>Editing a Course</h3><a href=\"my_database\" class=\"btn btn-info w-25\"><i class="fas fa-backward"></i>Back</a>
                <section class="col-sm-6 mt-2 mx-auto">
                    <form action="my_database?edit=%s&option=on" method="post">
                      <section>
                        <section class="form-group">
                          <label for="c_code">Course Code: <sup class="text-danger">*</sup></label>
                          <input type="text" name="c_code" class="form-control form-control-lg" value="%s" required>
                        </section>
                        <section class="form-group">
                          <label for="c_title">Course Title: </label>
                          <input type="text" name="c_title" class="form-control form-control-lg" value="%s">
                        </section>
                        <section class="form-group">
                          <label for="c_level">Course Level: </label>
                          <input type="number" name="c_level" class="form-control form-control-lg" value="%s" maxlength="3" required>
                        </section>
                        <section class="form-group">
                          <label for="c_unit">Course Unit: <sup class="text-danger">*</sup></label>
                          <input type="number" name="c_unit" class="form-control form-control-lg" value="%s" maxlength="1" required>
                          <span class="invalid-feedback"></span>
                        </section>
                        <section class="form-group">
                          <label for="c_score">My Score: <sup class="text-danger">*</sup></label>
                          <input type="number" name="c_score" class="form-control form-control-lg" value="%s" maxlength="3" required>
                          <span class="invalid-feedback"></span>
                        </section>
                      </section>

                          <input type="submit" value="Update Course in My Database" class="btn btn-warning btn-block">
                      </section>
                    </form>
                </section>
                """ % (one_course[1], one_course[1], one_course[2], one_course[3], one_course[4], one_course[5])
                all_contents = self.display.database_summary(display_breakdown_summary, tcourses, tunits, tcgpa, designate, edit_content)
            elif c_code != "" and c_level != "" and c_unit != "" and c_score != "" and edit != "" and delete == "" and option == "on":
                #EDITING A COURSE
                course_id = dbase.select_user_course(edit)[0][0]
                upc_grade = grades.generate_4_points(c_score)
                dbase.update_user_database(course_id, c_code, c_title, c_level, c_unit, c_score, upc_grade)
                edit_content = """<h3 class=\"display-5 d-inline-block w-75\">Editing a Course</h3><a href=\"my_database\" class=\"btn btn-info w-25\">My Database</a>
                <section class="col-sm-6 mt-2 mx-auto">
                    <label class="text-success">Course Updated Successfully!!!</label>
                </section>
                """
                all_contents = self.display.database_summary(display_breakdown_summary, tcourses, tunits, tcgpa, designate, edit_content)
            elif c_code == "" and c_level == "" and c_unit == "" and c_score == "" and edit == "" and delete != "" and option == "off":
                #DISPLAY COURSE TO DELETE
                one_course = dbase.select_user_course(delete)[0]
                delete_content = """
                <h3 class=\"display-5 d-inline-block w-75\"><i class="fas fa-trash-alt"></i>Deleting a Course</h3><a href=\"my_database\" class=\"btn btn-info w-25\"><i class="fas fa-backward"></i>Back</a>
                <section class="col-sm-6 mt-2 mx-auto">
                    <label>Course Title: %s</label><br/>
                    <label>Course Code: %s</label><br/>
                    <label>Course Level: %s</label><br/>
                    <label>Course Units: %s</label><br/>
                    <label>Course Score: %s</label><br/>
                    <a href=\"?delete=%s&option=on\" class="btn btn-warning">Delete This Course</a>
                </section>
                """ % (one_course[2], one_course[1], one_course[3], one_course[4], one_course[5], one_course[1])
                all_contents = self.display.database_summary(display_breakdown_summary, tcourses, tunits, tcgpa, designate, delete_content)
            elif c_code == "" and c_level == "" and c_unit == "" and c_score == "" and edit == "" and delete != "" and option == "on":
                #DELETING COURSE
                dbase.delete_user_database(delete)
                delete_content = """<h3 class=\"display-5 d-inline-block w-75\">Deleting a Course</h3><a href=\"my_database\" class=\"btn btn-info w-25\">My Database</a>
                <section class="col-sm-6 mt-2 mx-auto">
                    <label class="text-success">Course Deleted Successfully!!!</label>
                </section>
                """
                all_contents = self.display.database_summary(display_breakdown_summary, tcourses, tunits, tcgpa, designate, delete_content)


        return self.display.page_open(), self.display.page_nav(my_link[2]), self.display.database_form(), all_contents, self.display.page_close()
    my_database.exposed = True

    def exit_application(self):
        mainframe.engine.exit()
        exit_contents = """
<section class="col-sm-6 mx-auto text-center text-info">
    <label>You have exited the CGPA Application</label>
</section>
        """
        return self.display.page_open(), exit_contents, self.display.page_close()
    exit_application.exposed = True

#Initialization of application on custom server and port
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    conf = {"global": {"server.socket_host": '127.0.0.1', "server.socket_port": 3000, "server.thread_pool": 10}, "/": {"tools.staticdir.on": True, "tools.staticdir.dir": current_dir}}
    mainframe.quickstart(CummulativeGradePointAverage(), "/", config=conf)
