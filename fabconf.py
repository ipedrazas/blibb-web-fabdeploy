import os

from fabdeploy.api import DefaultConf


DIRNAME = os.path.dirname(__file__)


class BaseConf(DefaultConf):
    server_name = 'devblibb.com'
    server_admin = 'blibb@blibb.co'

    repo_origin = 'https://github.com/ipedrazas/blibb-web.git'


class StagingConf(BaseConf):
	server_name = 'blibb.co'
    sudo_user = 'fabdeploy'
    address = 'blibb_api@blibb.co'


class ProdConf(BaseConf):
	server_name = 'blibb.it'
    sudo_user = 'fabdeploy'
    address = 'blibb_web@blibb.it'


class LocalhostConf(BaseConf):
    address = 'blibb_web@localhost'
    sudo_user = 'ivan'
