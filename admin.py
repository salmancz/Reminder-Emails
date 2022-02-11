import streamlit as st
import smtplib, ssl
import csv

# Getting User Emails
filename = "members.csv"
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

bot_email = "salmandev.bot@gmail.com"
password = "salmanbotpass"
port = 587
smtp_server = "smtp.gmail.com"

st.title("Admin Home")
st.subheader("Mail Context")
st.empty()
mail_subject = st.text_input("Enter Subject : ")
mail_message  = st.text_area("Enter Message : ")
main_email_sender = st.button("Send Mail")

mail_content = """\
Subject: {0}
{1}

""".format(mail_subject, mail_message)

def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context = context)
        email.login(bot_email, password)
        for row in rows:
            for col in row:
                reciever_name, reciever_email = col.split()
                email.sendmail(bot_email, reciever_email, mail_content)

if main_email_sender:
    sendEmail()
    st.success("Mail sent successfully")
