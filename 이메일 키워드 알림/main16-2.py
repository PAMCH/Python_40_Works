import imaplib
import email
from email import policy

def find_encoding_info(txt) : # 메일 문자열 인코딩
    info = email.header.decde_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '네이버아이디'
pw = '네이버비밀번호'
imap.login(id,pw)

imap.select('INBOX') # 받은 메일에서 메일 가져오기
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:] # 최근 5개의 메일

for mail in reversed(last_email) : #최신 메일부터 볼수있게 뒤집어서 출력
    result, data = imap.uid('fetch',mail,'(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email,policy=policy.default)

    print('='*70)
    print('FROM:',email_message['From'])
    print('SENDER:',email_message['Sender'])
    print('TO:',email_message['To'])
    print('DATE:',email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:',subject)

    print('[CONTENT]')
    message = ' '
    if email_message.is_multipart() : 
        for part in email_message.get_payload() :
            if part.get_contest_type() == 'text/plain' : # 메일 본문이 text/plain인 경우에만
                bytes = part.get_payload(decode=True)
                encode = part.get_content_charset()
                message = message +str(bytes, encode)


    print('='*70)

imap.close
imap.logout