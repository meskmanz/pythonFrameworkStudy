class Config:
    def __init__(self, env):
        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not supported environment (supported envs: {SUPPORTED_ENVS})')

        self.base_url = {
            'dev': 'https://demo.opencart.com/',
            'qa': 'https://demo.opencart.ua/'
        }[env]
