import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = 'smtp.163.com'
mail_user = 'fionagu531'
mail_pass = 'YMHQNMXNQSCHEBJV'
sender = 'fionagu531@163.com'


def send_plain_mail(to,subject,body):
    message = MIMEText (body,'plain','utf-8')
    message['From'] = sender
    message['To'] = ','.join(to)
    message['Subject'] = Header(subject,'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host)
        smtpObj.login(mail_user, mail_pass)

        smtpObj.sendmail(sender, to, message.as_string())
        print('Mail Send!')
    except smtplib.SMTPException as e:
        print(e)


def send_html_mail(to, subject, body):
    message = MIMEText (body,'html','utf-8')
    message['From'] = sender
    message['To'] = ','.join(to)
    message['Subject'] = Header(subject,'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host)
        smtpObj.login(mail_user, mail_pass)

        smtpObj.sendmail(sender, to, message.as_string())
        print('Mail Send!')
    except smtplib.SMTPException as e:
        print(e)


def send_mail_with_attachments(to,subject,body,filelist):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ','.join(to)
    message['Subject'] = Header(subject,'utf-8')

    #邮件正文内容
    message.attach(MIMEText(body,'plain','utf-8'))

    '''根据filelist构造附件，传送当然目录下的filelist文件'''
    #当前执行文件所在的目录 和文件名
    dirname, temp = os.path.split(os.path.abspath(__file__))
    
    for filename in filelist:
        path2=os.path.join(dirname, filename)
        att = MIMEText(open(path2,'rb').read(),'base64','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename="'+filename+'"'
        message.attach(att)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host)
        smtpObj.login(mail_user, mail_pass)

        smtpObj.sendmail(sender, to, message.as_string())
        print('Mail Send!')
    except smtplib.SMTPException as e:
        print(e)


def test_send_plain_mail():
    receivers = ['fiona.gu.1@lexisnexis.com','zlandmin_1112@163.com']
    subject = 'Python SMTP - Plain text mail'
    body = '''
    <p>This is plain text email test body</p>
    <p><a href="http://www.baidu.coom">This is a link</a></p>
    '''

    send_plain_mail(receivers,subject, body)


def test_send_html_mail():
    receivers = ['fiona.gu.1@lexisnexis.com','zlandmin_1112@163.com']
    subject = 'Python SMTP - HTML format mail'
    body = '''
    <p>This is HTML format email test body</p>
    <p><a href="http://www.baidu.coom">This is a link</a></p>
    '''

    send_html_mail(receivers,subject, body)


def test_send_mail_with_attachments():
    receivers = ['fiona.gu.1@lexisnexis.com','zlandmin_1112@163.com']
    subject = 'Python SMTP - mail with attchments'
    body = 'Test send email with attachments'

    files = ['att1.txt','att2.txt']

    send_mail_with_attachments(receivers,subject, body,files)


if __name__=='__main__':
    # test_send_plain_mail()
    # test_send_html_mail()
    test_send_mail_with_attachments()
    

    

