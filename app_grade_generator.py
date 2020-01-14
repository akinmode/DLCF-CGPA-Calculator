class GradeGenerator(object):
    def generate_4_points(self, score):
        grade = ""

        if int(score) < 40:
            grade = 0
        elif 40 <= int(score) < 45:
            grade = 0
        elif 45 <= int(score) < 50:
            grade = 1
        elif 50 <= int(score) < 60:
            grade = 2
        elif 60 <= int(score) < 70:
            grade = 3
        elif 70 <= int(score) <= 100:
            grade = 4
        return grade

    def grade_scale_4_points(self, cgpa):
        scale = ""

        if cgpa < 1.0:
            self.scale = "Pass"
        elif 1.0 <= cgpa < 2.0:
            self.scale = "Third Class Honours"
        elif 2.0 <= cgpa < 3.0:
            self.scale = "Second Class Honours (Lower Division)"
        elif 3.0 <= cgpa < 3.5:
            self.scale = "Second Class Honours (Upper Division)"
        elif 3.5 <= cgpa <= 4.0:
            self.scale = "First Class Honours"
        return self.scale

    def generate_7_points(self, score):
        self.grade = ""
        if score < 40:
            self.grade = 0
        elif 40 <= score < 45:
            self.grade = 1
        elif 45 <= score < 50:
            self.grade = 2
        elif 50 <= score < 55:
            self.grade = 3
        elif 55 <= score < 60:
            self.grade = 4
        elif 60 <= score < 65:
            self.grade = 5
        elif 65 <= score < 70:
            self.grade = 6
        elif 70 <= score <= 100:
            self.grade = 7
        return self.grade

    def grade_scale_7_points(self, cgpa):
        self.scale = ""
        if cgpa < 1.6:
            self.scale = "Pass"
        elif 1.6 <= cgpa < 2.6:
            self.scale = "Third Class"
        elif 2.6 <= cgpa < 4.6:
            self.scale = "Second Class Lower"
        elif 4.6 <= cgpa < 6.0:
            self.scale = "Second Class Upper"
        elif 6.0 <= cgpa <= 7.0:
            self.scale = "First Class"
        return self.scale

    def grade_scale_msc_points(self, cgpa):
        self.scale = ""

        if cgpa < 1.0:
            self.scale = "Terminal"
        elif 1.0 <= cgpa < 2.0:
            self.scale = "Unknown"
        elif 2.0 <= cgpa < 3.0:
            self.scale = "MPhil"
        elif 3.0 <= cgpa < 3.5:
            self.scale = "MPhil/PhD"
        elif 3.5 <= cgpa <= 4.0:
            self.scale = "PhD Grade"
        return self.scale
