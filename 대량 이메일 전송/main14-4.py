import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

send_email = "구글 아이디@naver.com"
send_pwd = "구글앱 비밀번호"

recv_email = "받는 이메일@hanmail.net"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "HTML 테스트"
msg['From'] = send_email
msg['To'] = recv_email

html_body ="""
<p> 안녕하세요, HTML 형식 테스트 입니다.
"""

msg.attach(MIMEText(html_body,'html'))

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()