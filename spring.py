import sqlite3
import re
import math, random 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#import xlrd
import sys

conn = sqlite3.connect('spring.db')
cur = conn.cursor()
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


dicthtlt1 = {'1':850,'2':1110,'3':1200,'4':1200,'5':1000,'6':950,'7':2000,'8':1667,'9':1867,'10':2398}
dicthtlt2 = {'13':1850,'14':2010,'15':2040,'16':2000,'17':2040,'18':1950,'19':2500,'20':2567,'21':2267,'22':3098}
dicthtlt3 = {'25':2850,'26':3110,'27':3200,'28':2904,'29':3000,'30':3950,'40':3450,'41':3167,'42':3267,'43':4398}

def selectCity():
    z = int(input("For how many days you want to stay ?"))
    print("These are the list of adventure cities: \n1. Rishikesh\n2. Auli\n3. Kasauli\n4. Gulmarg\n5. Spiti")
    x = input()
    h = 0
    if(x == '1'):
        w = input("What kind of hotel are you looking for\na. Single sharing\nb. Twin bed\nc. Deluxe Double bed ??")
        if(w == 'a'):
            print("Please select the hotels by their respective id: \n1. Green Hotel -- 850/-\n2. Aloha on Ganges -- 1110/-")
            y = input()
            h =z*(h + dicthtlt1[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'b'):
            print("Please select the hotels by their respective id: \n13. Green Hotel -- 1850/-\n14. Aloha on Ganges -- 2010/-")
            y = input()
            h =z*(h + dicthtlt2[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'c'):
            print("Please select the hotels by their respective id: \n25. Green Hotel -- 2850/-\n26. Aloha on Ganges -- 3110/-")
            y = input()
            h =z*(h + dicthtlt3[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
    if(x == '2'): 
        w = input("What kind of hotel are you looking for\na. Single sharing\nb. Twin bed\nc. Deluxe Double bed ??")
        if(w == 'a'):
            print("Please select the hotels by their respective id: \n3. Stunning Hills -- 1200/-\n4. Hotel Giriganga -- 1200/-")
            y = input()
            h =z*(h + dicthtlt1[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'b'):
            print("Please select the hotels by their respective id: \n15. Stunning Hills -- 2040/-\n16. Hotel Giriganga -- 2000/-")
            y = input()
            h =z*(h + dicthtlt2[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'c'):
            print("Please select the hotels by their respective id: \n27. Stunning Hills -- 3200/-\n28. Hotel Giriganga -- 2904/-")
            y = input()
            h =z*(h + dicthtlt3[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
    if(x == '3'):
        w = input("What kind of hotel are you looking for\na. Single sharing\nb. Twin bed\nc. Deluxe Double bed ??")
        if(w == 'a'):            
            print("Please select the hotels by their respective id: \n5. Kasauli Castle -- 1000/-\n6. Kasauli Exotica -- 950/-")
            y = input()
            h =z*(h + dicthtlt1[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'b'):
            print("Please select the hotels by their respective id: \n17. Kasauli Castle -- 2040/-\n18. Kasauli Exotica -- 1950/-")
            y = input()
            h =z*(h + dicthtlt2[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'c'):
            print("Please select the hotels by their respective id: \n29. Kasauli Castle -- 3000/-\n30. Kasauli Exotica -- 3950/-")
            y = input()
            h =z*(h + dicthtlt3[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
    if(x == '4'):
        w = input("What kind of hotel are you looking for\na. Single sharing\nb. Twin bed\nc. Deluxe Double bed ??")
        if(w == 'a'):
            print("Please select the hotels by their respective id: \n7. Hotel Marina -- 2000/-\n8. Khyber Himalaya -- 1667/-")
            y = input()
            h =z*(h + dicthtlt1[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'b'):
            print("Please select the hotels by their respective id: \n19. Hotel Marina -- 2500/-\n20. Khyber Himalaya -- 2567/-")
            y = input()
            h =z*(h + dicthtlt2[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'c'):
            print("Please select the hotels by their respective id: \n40. Hotel Marina -- 3450/-\n41. Khyber Himalaya -- 3167/-")
            y = input()
            h =z*(h + dicthtlt3[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
    if(x == '5'):
        w = input("What kind of hotel are you looking for\na. Single sharing\nb. Twin bed\nc. Deluxe Double bed ??")
        if(w == 'a'):
            print("Please select the hotels by their respective id: \n9. Spiti Valley -- 1867/-\n10. Spiti Sarai -- 2398/-")
            y = input()
            h =z*(h + dicthtlt1[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'b'):
            print("Please select the hotels by their respective id: \n21. Spiti Valley -- 2267/-\n22. Spiti Sarai -- 3098/-")
            y = input()
            h =z*(h + dicthtlt2[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))
        if(w == 'c'):
            print("Please select the hotels by their respective id: \n42. Spiti Valley -- 3267/-\n43. Spiti Sarai -- 4398/-")
            y = input()
            h =z*(h + dicthtlt3[y])
            print("Thanks for choosing, your hotel bill is: "+str(h))

def insertion():
    
    global name
    global age
    global email
    global mob
    global per
    global uname
    global pswd
    cur.execute("INSERT INTO reg(name,age,email,mob,per,uname,pswd) VALUES (:name,:age,:email,:mob,:per,:uname,:pswd)",{'name':n,'age':ag,'email':e,'mob':mob,'per':per,'uname':u,'pswd':p})
    conn.commit()
    
def validation(email):
    
    if(re.search(regex,email)):
       
        sendEmail()
        otpcheck()
    else:  
        print("Invalid Email")  
    
def pswdval():
    passwd = p
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)                   
    mat = re.search(pat, passwd)   
    if mat: 
        validation(e)
    else: 
        print("Password invalid !!...\n1. Should have at least one number.\n2. Should have at least one uppercase and one lowercase character.\n3. Should have at least one special symbol.\n4. Should be between 6 to 20 characters long.") 

def age():
    if ag > 18:
        
        pswdval()
    else:
        print("Sorry you are minor\nMinimum age required is 18...")

digits = "0123456789"
OTP = ""  
for i in range(4) : 
    OTP += digits[math.floor(random.random() * 10)] 
    
def sendEmail():
    email = "ishaansharma.aries@gmail.com"
    password = "@bst3rg0AZ5"
    send_to_email = e
    subject = "Springfield Adventures Registration"
    message = "Hello " + n + " your OTP is "+ str(OTP) +" \nWith Username: "+ u
    
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg["Subject"] = subject
    
    msg.attach(MIMEText(message,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email,password)
    text = msg.as_string()
    server.sendmail(email,send_to_email,text)
    server.quit()

def otpcheck():
    o = input("Please enter the otp: ")
    if o == OTP:
        print("You have been registered to Springfield Adventures.")
        insertion()
    else:
        print("Wrong OTP")
        sys.exit1()
def login():
       print("SPRINGFIELD ADVENTURES")
       unam = input("Please enter your username: ")
       psswd = input("Please enter the password: ")
       cur.execute("SELECT * FROM reg WHERE uname = :uname AND pswd = :pswd",{'uname':unam,'pswd':psswd})
       results = cur.fetchall()
       if(results):    
           print("Welcome " + unam)
           lgdata()
       else:
           print("Username and password doesnot exists")

def lgdata():
    print("Do you wish to continue in checking the cities ?\n If YES type 'y'\ If NO type 'n'")
    x = input()
    if(x == 'y'):
        selectCity()
    elif(x == 'n'):
        sys.exit()
    else:
        print("Invalid input")




print("SPRINGFIELD ADVENTURES")
print("Please select the option:\n1.Login \n2.Signup")
a = int(input("Enter input here: "))
if(a == 2):
    print("Please enter the following details: ")
    n = input("Enter name: ")
    ag = int(input("Enter age: "))
    e = input("Enter email: ")
    mob = int(input("Enter mobile number: "))
    per = int(input("Enter the number of persons: "))
    u = input("Enter username: ")
    p = input("Enter password: ")
    age()
elif(a == 1):
    login()    
else:
    print("Invalid input")

conn.commit()
conn.close()