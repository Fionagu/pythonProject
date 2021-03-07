class Config():
    def __init__(self, env):
        self.base_url ={
            "dev":"http://dev-env.com",
            "cert":"http://cert-env.com"
        }[env]

        self.port = {
            "dev":8080,
            "cert":80
        }[env]
