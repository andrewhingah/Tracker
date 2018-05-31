import os
class Config(object):
	Debug=False
	CSRF_ENABLED=True
	SECRET=os.getenv('SECRET')

class DevelopmentConfig(Config):
	"""configurations for development"""
	DEBUG=True

class TestingConfig(Config):
	TESTING = True
	DEBUG = True

class StagingConfig(Config):
    #Configurations for Staging#
    DEBUG = True

 class ProductionConfig(Config):
 	DEBUG = False
 	TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
   
}
