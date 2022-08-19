# -*- coding: utf-8 -*-
"""


@author: Irfan
"""
            #send email using python
import smtplib
my_email = "xxxx@.com"
password = "xxxx"
 
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = papassword)

connection.sendmail(from_addr = my_email,
                    to_addrs = "receipentemail@gmail.com", msg ="Hello world")

connection.close()









