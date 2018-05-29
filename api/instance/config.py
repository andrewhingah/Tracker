import os
class Config(object):
	Debug=False
	CSRF_ENABLED=True
	SECRET=os.getenv('SECRET')

class DevelopmentConfig(Config):
	"""configurations for development"""
	DEBUG=True

class StagingConfig(Config):
    #Configurations for Staging#
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
