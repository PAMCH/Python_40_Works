import imaplib
import email
from email import policy
import requests
import json
import time # 반복 수행을 위함

slack_webhook_url = '슬랙 웹 주소'

def sendSlackWebhook(strText) :
    headers = {
        "Content-type" : "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else :
        return "error"

def find_encoding_info(txt) :
    info = email.header.decde_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '네이버아이디'
pw = '네이버비밀번호'
imap.login(id,pw)

send_list = []

while True :
    try :
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-5:]

        for mail in reversed(last_email)
            result, data = imap.uid('fetch',mail,'(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email,policy=policy.default)

            email_from = str(email_message['From'])
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)

            if subject_str.find("정상") >= 0 :
                slack_sned_message = email_from + '\n' + email_date + '\n' + subject_str
                if slack_sned_message not in send_list : # 새로운 메시지만 알림을 위함
                    sendSlackWebhook(slack_sned_message)
                    print(slack_sned_message)
                    send_list.append(slack_sned_message) # 새로운 메시지를 리스트에 추가

        time.sleep(30) # 30초마다 실행
    except KeyboardInterrupt : # 키보드 인터럽트 발생 시 종료
        break

imap.close()
imap.logout()