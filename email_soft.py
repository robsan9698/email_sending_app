import smtplib , webbrowser
def get_mail():
    servicesAvailable = ['hotmail' , 'gmail' , 'yahoo' , 'outlook']
    while True:
        mail_id = input("Email : ")
        if '@' in mail_id and '.com' in mail_id:
            #robin.iitm16@gmail.com
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvailable:
                return mail_id , sp
                break
            else:
                print("we don't provide services for " + sp)
                print("we provide service only for : hotmail/outlook,yahoo,gmail")
                continue
        else:
            print("Invalid Email !!! Retype Again")


def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail' :
        return 'smtp.gmail.com'
    elif serviceProvider == 'outlook' or serviceProvider == 'hotmail':
        return 'smtp-mail.outlook.com'
    elif serviceProvider == 'yahoo':
        return 'smtp.mail.yahoo.com'



user_mail , sp = get_mail()
smtpDomain = set_smtp_domain(sp)

print('Welcome you can send an E-mail through this program ')
print('Please enter your email address and password : ')
e_mail, serviceProvider = get_mail()
print("your service provider is " + serviceProvider)
password = input("Password: ")


while True:
    try:
        smtpDomain = set_smtp_domain(serviceProvider)
        connection = smtplib.SMTP(smtpDomain , 587)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail , password)

    except:
        if serviceProvider == 'gmail':
            print("Login unsuccessful , there are two possible reasons :")
            print("1.) You typed wrong username or password")
            print("2.) You are using Gmail with less secure Apps  option turned off")
            print(" Do you want to turn on the option of less secure Apps")
            answer = input("yes or no ? : ")
            if answer == "yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            else:
                print("Pls!! enable the less secure option . Visit the link https://myaccount.google.com/lesssecureapps")

            print("Please retype your email and password")
            e_mail , serviceProvider = get_mail()
            password = input("Password : ")
            continue
        else:
            print("Login unsuccessful , Pls. check your email Id and Password and Try again")
            print("Please retype your e-mail address and password")
            e_mail , serviceProvider = get_mail()
            password =input("Password : ")
            continue
    else:
        print(" Login successful ")
        break
print("Please type receiver's E-mail address")
receiverAddress , receiverSp = get_mail()
print("Now please type Subject and Message")
Subject = input("Subject: ")
Message = input("Message: ")
connection.sendmail(e_mail , receiverAddress , ("Subject: " +str(Subject) + "\n\n" + str(Message)))
print("E-mail send successfully")
connection.quit()
