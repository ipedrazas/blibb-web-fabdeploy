import os

from fabdeploy.api import DefaultConf


DIRNAME = os.path.dirname(__file__)


class BaseConf(DefaultConf):
    server_name = 'blibb.co'
    server_admin = 'blibb@blibb.com'

    repo_origin = 'https://github.com/ipedrazas/blibb-web.git'


class StagingConf(BaseConf):
    sudo_user = 'fabdeploy'
    address = 'blibb_api@176.31.103.197'


class ProdConf(BaseConf):
    sudo_user = 'fabdeploy'
    address = 'blibb_web@176.31.103.197'


class LocalhostConf(BaseConf):
    address = 'blibb_web@localhost'
    sudo_user = 'vmihailenco'
