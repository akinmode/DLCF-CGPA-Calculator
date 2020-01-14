class HtmlTable(object):
    openTable = "<h3 class=\"display-5\"><i class=\"fas fa-database\"></i>My Courses</h3><table class=\"table table-dark\">"
    closeTable = "</table>"
    headersTable = ""
    contentsTable = ""

    def add_headers(self, headers = []):
        if headers == []:
            self.headersTable = ""
        elif headers != []:
            headers = ["<th scope=\"col\">"+str(each)+"</th>" for each in headers]
            htable = "".join(headers)
            self.headersTable = "<thead><tr>"+htable+"</tr></thead>"

    def add_rows(self, contents = []):
        if contents == []:
            self.contentsTable = ""
        elif contents != []:
            allContent = []
            for eachrow in contents:
                rows = ["<td scope=\"col\">"+str(eachcell)+"</td>" for eachcell in eachrow]
                rows[0] = "<tr>"+rows[0]
                rows[-1] = rows[-1]+"<td><a href=\"?edit="+eachrow[0]+"&option=off\" class=\"btn btn-info btn-block\" style=\"font-size:60%;\"><i class=\"fas fa-edit\"></i>Edit</a></td><td><a href=\"?delete="+eachrow[0]+"&option=off\" class=\"btn btn-danger btn-block\" style=\"font-size:60%;\"><i class=\"fas fa-trash-alt\"></i>Delete</a></td></tr>"
                allContent.append("".join(rows))
            self.contentsTable = "<tbody>"+"".join(allContent)+"</tbody>"

    def show_table(self):
        allTable = [self.openTable, self.headersTable, "".join(self.contentsTable), self.closeTable]
        return "".join(allTable)
