import requests, os, sys
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(receivers, subject, content, html):
    mail_host="xxx"
    mail_user="xxx"    
    mail_pass="xxx!" 

    sender = 'xxx@xxx.com'

    if (html=='html'):
        msg =  MIMEText(content, _subtype='html')
    else:
        msg =  MIMEText(content, _subtype='plain')
    msg['Subject'] = subject
    msg['From'] = 'xxx'
    msg['To'] = ','.join(receivers)  

    print(mail_host)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host) 
        server.sendmail(sender, receivers, msg.as_string()) 
        server.close()
        print('mail send')
    except smtplib.SMTPException:
        print('Error: mail send')


def get_report(url):
    res = requests.get(url)
    print(res.status_code)
    bs = BeautifulSoup(res.text, 'html.parser')

    table = bs.select('#tablesorter')[0]

    style = '''
    <style>
        a {
            color: #0097da;
        }
        a:hover {
            color: #00587f;
        }
        .passed {
            background-color: #92DD96;
        }
        .failed {
            background-color: #F2928C;
        }
        .skipped {
            background-color: #8AF;
        }
        .pending {
            background-color: #F5F28F;
        }
        .undefined {
            background-color: #F5B975;
        }
        table{
            border-collapse: collapse;
        }
        table,table th { 
            border:1px solid #ccc; 
        }
        table,table tr td { 
            border:1px solid #ccc; 
        }
        .footer {
            font-size: smaller;
            text-align: center;
            margin-top: 30px;
        }
    </style>
    '''
    content = style + str(table)
    return content

if (__name__=='__main__'):
    build_url =  sys.argv[1]
    env =  sys.argv[2]
    branch =  sys.argv[3]
    tags =  sys.argv[4]
    email_to =  sys.argv[5]
    # build_url = os.getenv("BUILD_URL")
    # env = os.getenv("ENV")
    # branch = os.getesnv("BRANCH")
    # tags = os.getenv("TAGS")
    # email_to = os.getenv("EMAIL")

    report_url = build_url + 'cucumber-html-reports/overview-features.html'

    print('========build url=========')
    print(build_url)

    print('========report url=========')
    print(report_url)

    print('========env=========')
    print(env)

    print('========tags=========')
    print(tags)

    print('========email=========')
    print(email_to)


    receivers = email_to.split(',')
    subject = 'APAC Webservice Report on '+ env
    report = get_report(report_url)

    env_info = '<p>env: '+env+'</p>'
    branch_info = '<p>branch: '+branch+'</p>'
    tags_info = '<p>tags: '+tags+'</p>'
    build_info = '<p>Build URL: '+build_url.replace('localhost', 'lngshal-176')+'</p>'
    artifact_info = '<p>Artifact: '+build_url.replace('localhost', 'lngshal-176')+'artifact/</p>'
    
    content = env_info+ branch_info+tags_info+build_info + artifact_info+ report

    send_mail(receivers, subject, content, 'html')