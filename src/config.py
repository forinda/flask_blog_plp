import os

class ProductionConfig(object):
	pass
	
class DevelopmentConfig(object):
	pass
	
class TestingConfig(object):
	pass
	
class StagingConfig(object):
	pass
	
config = {
	"dev":DevelopmentConfig,
	"prod":ProductionConfig,
	"test":TestingConfig,
	"stage":StagingConfig
}
