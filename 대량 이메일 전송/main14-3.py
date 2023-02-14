import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

send_email = "구글 아이디@naver.com"
send_pwd = "구글앱 비밀번호"

recv_email = "받는 이메일@hanmail.net"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart() # 복합형식으로 메시지 형식을 선언하여 첨부파일 추가 가능

msg['Subject'] = "첨부파일 테스트"
msg['From'] = send_email
msg['To'] = recv_email

text = """
첨부파일 테스트
잘 작동되는지 봅니다.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'\\첨부파일.txt'

with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition', 'attachment', filename="첨부파일.txt")
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()