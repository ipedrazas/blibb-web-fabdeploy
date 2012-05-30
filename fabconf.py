import os

from fabdeploy.api import DefaultConf


DIRNAME = os.path.dirname(__file__)


class BaseConf(DefaultConf):
    
    server_admin = 'blibb@blibb.co'

    repo_origin = 'https://github.com/ipedrazas/blibb-web.git'


class StagingConf(BaseConf):
	server_name = 'blibb.co'
	sudo_user = 'fabdeploy'
	address = 'blibb_web@blibb.co'
	api_url = 'http://api.blibb.co'


class ProdConf(BaseConf):
	server_name = 'blibb.it'
	sudo_user = 'fabdeploy'
	address = 'blibb_web@blibb.it'
	api_url = 'http://api.blibb.it'

class DevConf(BaseConf):
    server_name = 'blibb.es'
    sudo_user = 'fabdeploy'
    address = 'blibb_web@blibb.es'
    api_url = 'http://api.blibb.es'

class LocalhostConf(BaseConf):
	server_name = 'devblibb.com'
	address = 'blibb_web@localhost'
	sudo_user = 'ivan'
	api_url = 'http://api.devblibb.com'
