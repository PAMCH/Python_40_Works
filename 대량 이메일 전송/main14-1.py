import smtplib # 메일 전송을 위한 모듈
from email.mime.text import MIMEText

send_email = "네이버 아이디@naver.com"
send_pwd = "네이버 비밀번호"

recv_email = "받는 이메일@hanmail.net"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
메일 본문
여러줄 가능
"""

msg = MIMEText(text) # 메시지를 텍스트 형식으로 지정

msg['Subject'] = "메일 제목"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
