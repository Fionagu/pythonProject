import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(receivers, subject, content, html):
    # 第三方 SMTP 服务
    mail_host="smtp.163.com"  #设置服务器
    mail_user="xxx"    #用户名
    mail_pass="xxx"   #口令 

    sender = 'xxx@163.com'

    if (html=='html'):
        msg =  MIMEText(content, _subtype='html')
    else:
        msg =  MIMEText(content, _subtype='plain')
    msg['Subject'] = subject
    msg['From'] = 'xxx@gmail.com'
    msg['To'] = ','.join(receivers)   #以逗号隔开的收件人邮箱

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(sender, receivers, msg.as_string())  #receivers是一个array
        server.close()
        print('mail send')
    except smtplib.SMTPException:
        print('Error: mail send')


if (__name__=='__main__'):
    receivers = ['xxx@gmail.com']

    html_subject = 'Test html email'
    html_content = '''
        <html>
        <p>this is a p</p>
        <p><a href='http://www.runoob.com'>this is a link</a></p>
        </html>
        '''
        
    plain_subject = 'Test plain email'
    plain_content = "this is plain content"

    # send_mail(receivers, html_subject, html_content, 'html')
    send_mail(receivers, plain_subject, plain_content, 'plain')