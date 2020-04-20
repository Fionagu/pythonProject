import io
from xml.dom.minidom import parse

configJosn = {
    'dev4': {
        'file': 'C:\inetpub\wwwroot\\nl_dev4\Web.config',
        'primaryServiceHost': 'http://ddc4c-i-services.route53.lexis.com',
        'authServiceHost': 'https://ddc4-signin.lexisnexis.com'
    },
    'cert7': {
        'file': 'C:\inetpub\wwwroot\\nl_cert7\Web.config',
        'primaryServiceHost': 'http://cdc7c-i-services.route53.lexis.com',
        'authServiceHost': 'https://cdc13-signin.lexisnexis.com'
    },
    'cert2': {
        'file': 'C:\inetpub\wwwroot\\nl_cert2\Web.config',
        'primaryServiceHost': 'http://cdc2c-i-services.route53.lexis.com',
        'authServiceHost': 'https://cdc1-signin.lexisnexis.com'
    }
}


# print(configJosn[env]['file'])

# print(configJosn[env]['primaryServiceHost'])
# print(configJosn[env]['authServiceHost'])

def update_config(env):
    configFile = configJosn[env]['file']
    domTree = parse(configFile)

    # #root
    # rootNode = domTree.documentElement

    #find appSettings node
    appSettingsNode = domTree.getElementsByTagName('appSettings')[0]

    #new a node
    skipBucketConnectionNode = domTree.createElement('add')
    skipBucketConnectionNode.setAttribute('key','SkipBucketConnection')
    skipBucketConnectionNode.setAttribute('value','true')

    appSettingsNode.appendChild(skipBucketConnectionNode)

    with open(configFile, 'w') as f:
        domTree.writexml(f, addindent= '    ', encoding= 'utf-8')


update_config('dev4')