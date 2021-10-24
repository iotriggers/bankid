#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb
import model

#Import Personnummer module
import personnummer

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
pnr  = form.getvalue('pnr')

#Validate pnr
result = "Invalid"
if personnummer.valid(pnr):
    result = "Valid"
    client = model.BankIdModel(pnr)
    response = client.auth()
    #print(response)    


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Personnummer: %s is %s</h2>" % (pnr,result) )
print ("</body>")
print ("</html>")