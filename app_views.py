class View(object):
    def page_open(self):
        pageOpen = """
<!DOCTYPE HTML>
<html>
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 <meta http-equiv="X-UA-Compatible" content="ie=edge">
 <meta name="description" content="">
 <meta name="author" content="">
 <link rel="icon" href="dlcf_logo.png">
	<link rel="stylesheet" href="bootstrap.min.css" type="text/css">
    <link href="fontawesome-all.css" rel="stylesheet">
<title>Cummulative Grade Calculator</title>
</head>
<body>
<section class="jumbotron container">
<h3 class="display-4 text-center">Cummulative Grade Calculator</h3>
<p class="text-center">Calculating Student Cummulative Point Average</p>
        """
        return pageOpen

    def page_close(self):
        pageClose = """
<hr/>
        <section class="text-center mt-3">
        <p class="mt-1"><label for="">Designed by DLCF Academic & ICT Directorate 2018.</label></p>
    </section>
 </section>
 <script src="jquery.min.js"></script>
	<script src="bootstrap.min.js"></script>
	<script src="main.js"></script>
 </body>
 </html>

        """
        return pageClose

    def page_nav(self, my_link = ""):
        if my_link == "":
            my_database_link = ""
        else:
            my_database_link = """
            <li class="nav-item">
              <a class="nav-link" href="my_database"><i class="fas fa-database"></i>My Database</a>
            </li>
            """
        pageNav = """
<!--NAVIGATION GOES HERE-->
<nav class="navbar navbar-expand-md mb-1">
  <section class="container-fluid">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarDefault" aria-controls="navbarDefault" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <section class="collapse navbar-collapse" id="navbarDefault">
      <!--LEFTHAND NAVBAR-->
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="index"><i class="fas fa-home"></i>Home</a>
        </li>
          %s
      </ul>

      <!--RIGHTHAND NAVBAR-->
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="exit_application"><i class="fas fa-eject"></i>Close Application</a>
          </li>
        </ul>
    </section>
  </section>
</nav>
        """ % (my_database_link)
        return pageNav

    def index_form(self):
        indexForm = """
<section class="row">
    <section class="col-sm-4">
        <form action="index" method="POST">
             <section class="form-group">
                 <label for="cgpa_number">Matric Number<sup class="text-danger">*</sup></label>
                 <input type="text" name="cgpa_number" class="form-control form-control-lg" placeholder="Matric Number" required>
                 <span class="invalid-feedback"></span>
             </section>
             <section class="form-group">
                 <label for="cgpa_names">Names<sup class="text-danger">*</sup></label>
                 <input type="text" name="cgpa_names" class="form-control form-control-lg" placeholder="Names" required>
                 <span class="invalid-feedback"></span>
             </section>
             <section class="form-group">
                 <label for="cgpa_cat">Category<sup class="text-danger">*</sup></label><br/>
                 <label class="form-check-label"><input class="form-check-input" type="radio" name="cgpa_cat" value="UG"> (UG)Undergraduates</label>
                 &nbsp;&nbsp;
                 <label class="form-check-label"><input class="form-check-input" type="radio" name="cgpa_cat" value="PG"> (PG)Postgraduates</label>
             </section>

             <input type="submit" value="Initialize My Application" class="btn btn-success btn-block">
         </form>
    </section>

    <section class="col-sm-8" style="font-size: 95%;">
        <h3>Knowledge they say is power</h3>
        <p>
            Knowledge is great, because knowledge translates you into a better person and changes your status.
            It is very commendable that you are seeking knowledge on how to plan and have good grades, but there are some knowledge that are indispensable.
            <ul>
            <li>Knowledge about the brevity of paper knowledge</li>
            <li>Knowledge about the brevity of life</li>
            <li>Knowledge about the day we will stand before our Creator</li>
            </ul>
        </p>
        <p>
            <label style="text-indent: 2em;">Do you know that our stay on earth is temporal?</label><br/>
            <label style="text-indent: 4em;">Do you that someday stand before our maker?</label><br/>
            <label style="text-indent: 6em;">Do you know the whole world is guilty before God?</label><br/>
            <label style="text-indent: 2em;">You stand condemned with the world already</label>
        </p>
        <p>
            <label><em><strong>“All have sinned and come short to the glory of God”</strong></em> Romans 3:23</label><br/>
            But the chiefest of all knowledge comes when you have an understanding that a provision was made at Calvary for you stand guiltless.
            Jesus death was that provision.
        </p>
        <p>
            <label><em><strong>“For God hath made him to be sin for us, who knew no sin, that we might be made the righteousness of God in him”</strong></em> II Corinthians 5:21</label><br/>
            Jesus paid the price for you to stand guiltless before God.
            Accept his offer, this knowledge pays forever and supercedes every other knowledge.
        </p>
    </section>
</section>
        """
        return indexForm

    def index_welcome(self, username, userid):
        indexWelcome = """
<h3 class="display-5 text-center">Welcome to The Assembly of Saintly Scholars, %s </h3>
<section class="w-75 mx-auto">
    <h3>Knowledge they say is power</h3>
    <p>
        Knowledge is great, because knowledge translates you into a better person and changes your status.
        It is very commendable that you are seeking knowledge on how to plan and have good grades, but there are some knowledge that are indispensable.
        <ul>
        <li>Knowledge about the brevity of paper knowledge</li>
        <li>Knowledge about the brevity of life</li>
        <li>Knowledge about the day we will stand before our Creator</li>
        </ul>
    </p>
    <p>
        <label style="text-indent: 2em;">Do you know that our stay on earth is temporal?</label><br/>
        <label style="text-indent: 4em;">Do you that someday stand before our maker?</label><br/>
        <label style="text-indent: 6em;">Do you know the whole world is guilty before God?</label><br/>
        <label style="text-indent: 2em;">You stand condemned with the world already</label>
    </p>
    <p>
        <label><em><strong>“All have sinned and come short to the glory of God”</strong></em> Romans 3:23</label><br/>
        But the chiefest of all knowledge comes when you have an understanding that a provision was made at Calvary for you stand guiltless.
        Jesus death was that provision.
    </p>
    <p>
        <label><em><strong>“For God hath made him to be sin for us, who knew no sin, that we might be made the righteousness of God in him”</strong></em> II Corinthians 5:21</label><br/>
        Jesus paid the price for you to stand guiltless before God.
        Accept his offer, this knowledge pays forever and supercedes every other knowledge.
    </p>
</section>
<label class="text-center"><a href='index?delete=%s'><i class="fas fa-edit"></i>Edit User</a></label>
        """  % (username.upper(), userid)
        return indexWelcome

    def database_form(self):
        databaseForm = """
<form action="my_database" method="post" id="database-form">
  <section class="row">
    <section class="form-group col-sm">
      <label for="c_code">Course Code: <sup class="text-danger">*</sup></label>
      <input type="text" name="c_code" class="form-control form-control-lg" placeholder="e.g. CHE157" required>
    </section>
    <section class="form-group col-sm">
      <label for="c_title">Course Title: </label>
      <input type="text" name="c_title" class="form-control form-control-lg" placeholder="e.g. Physical Chemistry">
    </section>
    <section class="form-group col-sm">
      <label for="c_level">Course Level: </label>
      <input type="number" name="c_level" class="form-control form-control-lg" placeholder="e.g. 100" maxlength="3" min="100" max="800" step="100" required>
    </section>
    <section class="form-group col-sm">
      <label for="c_unit">Course Unit: <sup class="text-danger">*</sup></label>
      <input type="number" name="c_unit" class="form-control form-control-lg" placeholder="e.g. 3 or 4" maxlength="1" required>
      <span class="invalid-feedback"></span>
    </section>
    <section class="form-group col-sm">
      <label for="c_score">My Score: <sup class="text-danger">*</sup></label>
      <input type="number" name="c_score" class="form-control form-control-lg" placeholder="score" maxlength="3" required>
      <span class="invalid-feedback"></span>
    </section>
  </section>

  <section class="row">
    <section class="col-sm">
      <input type="submit" value="Add Course to Database" class="btn btn-success btn-block" id="click-to-refresh">
    </section>

    <section class="col-sm">
     <a href="my_database" class="btn btn-info btn-block">View Updated Courses</a>
    </section>
  </section>
</form>
        """
        return databaseForm


    def database_summary(self, breakdown_summary, tcourses, tunits, tcgpa, designate, others_table):
        databaseSummary = """
<section class='row mt-1 mb-3 p-2'>
    <section class="col-sm-4" style="min-height: 200px;">
    <h3 class="display-5">Summary</h3>
    <p class='text-center text-success'>CGPA Computation Complete!</p>
    %s<br/>
    <label><strong><u>CUMMULATIVE</u></strong></label><br/>
    <label>Total Number of Courses: <span><em><strong>%s</strong></em></span></label><br/>
    <label>Total Number of Units: <span><em><strong>%s</strong></em></span></label><br/>
    <label>Cummulative Grade Point Average: <span><em><strong>%s</strong></em></span></label><br/>
    <label>Designation: <span><em><strong>%s</strong></em></span></label><br/>
    </section>

    <section class="col-sm-8 border-left" style="min-height: 200px;">
    %s
    </section>
</section>
        """ % (breakdown_summary, tcourses, tunits, tcgpa, designate, others_table)
        return databaseSummary

    def about_cgpa_page(self):
        aboutCgpaPage = """
<h3 class="display-7">About Cummulative Grade Calculator</h3>
<p></p>

        """
        return aboutCgpaPage
