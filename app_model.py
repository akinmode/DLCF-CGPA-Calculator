from app_database import Database

class Model(Database):
    def __init__(self):
        Database.__init__(self)
        #Create connection to database for application.
        self.pointer.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, matric_number integer, names text, category text)")
        self.pointer.execute("CREATE TABLE IF NOT EXISTS user_database (id INTEGER PRIMARY KEY, course_code text UNIQUE, course_title text, course_level integer, course_unit integer, course_score integer, course_grade integer)")
        self.connection.commit()

    def insert_user(self, a, b, c):
        self.pointer.execute("INSERT INTO user VALUES (NULL,?,?,?)",(a, b, c,))
        self.connection.commit()

    def view_user(self):
        self.pointer.execute("SELECT * FROM user")
        rows = self.pointer.fetchall()
        return rows

    def delete_user(self, a):
        self.pointer.execute("DELETE FROM user WHERE id=?",(a,))
        self.connection.commit()

############ USER DATABASE METHODS
    def view_user_database(self):
        self.pointer.execute("SELECT course_code, course_title, course_level, course_unit, course_score, course_grade FROM user_database ORDER BY course_level ASC")
        rows = self.pointer.fetchall()
        return rows

    def select_user_course(self, a):
        self.pointer.execute("SELECT * FROM user_database WHERE course_code=?",(a,))
        rows = self.pointer.fetchall()
        return rows

    def insert_user_database(self, a, b, c, d, e, f):
        self.pointer.execute("INSERT INTO user_database VALUES (NULL,?,?,?,?,?,?)",(a, b, c, d, e, f))
        self.connection.commit()

    def update_user_database(self, g, a, b, c, d, e, f):
        self.pointer.execute("UPDATE user_database SET course_code=?, course_title=?, course_level=?, course_unit=?, course_score=?, course_grade=? WHERE id=?",(a, b, c, d, e, f, g))
        self.connection.commit()

    def delete_user_database(self, a):
        self.pointer.execute("DELETE FROM user_database WHERE course_code=?",(a,))
        self.connection.commit()

    def general_summary(self):
        self.pointer.execute("SELECT COUNT(course_code), SUM(course_unit), SUM(course_grade*course_unit) FROM user_database")
        summed = self.pointer.fetchall()
        return summed

    def breakdown_summary(self):
        self.pointer.execute("SELECT course_level, COUNT(course_code), SUM(course_unit), SUM(course_grade*course_unit) FROM user_database GROUP BY course_level")
        bsummed = self.pointer.fetchall()
        return bsummed

    def __del__(self):
        self.connection.close()
