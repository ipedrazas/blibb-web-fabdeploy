from fabdeploy import monkey; monkey.patch_all()
from fabric.api import *
from fabric.contrib import files
from fabdeploy.api import *; setup_fabdeploy()
from fabdeploy.utils import upload_config_template, upload_init_template


class PhpPushNginxConfig(nginx.PushConfigTask):
    @conf
    def config_template(self):
        return 'nginx_php.config'

php_push_nginx_config = PhpPushNginxConfig()


@task
def user_create():
    users.create.run()
    ssh.push_key.run(pub_key_file='~/.ssh/id_rsa.pub')


def php_add_extension(extension):
    filename = '/etc/php5/fpm/php.ini'
    section = "Dynamic Extensions"
    line = "extension=%s" % extension

    if not files.contains(filename, line):
        line_number = int(sudo("awk '/%s/{print FNR}' %s" % (section, filename)))
        sudo("sed -i.bak '%s a\%s' %s" % (line_number + 2, line, filename))


@task
def php_install():
    system.package_install.run(packages='php5 php5-fpm')
    system.package_install.run(
        packages='php5-curl php5-gd php-pear php5-memcache')

    files.sed(
        '/etc/php5/fpm/pool.d/www.conf',
        '127.0.0.1:9000',
        '/var/run/php5-fpm.socket',
        use_sudo=True)


@task
def php_zmq_install():
    with settings(warn_only=True):
        sudo('pear channel-discover pear.zero.mq')
        sudo('pecl install zero.mq/zmq-beta')
    php_add_extension('zmq.so')


@task
def php_redis_install():
    with settings(warn_only=True):
        sudo('pear channel-discover pear.nrk.io')
        sudo('pear install nrk/Predis')


@task
def php_mongo_install():
    with settings(warn_only=True):
        sudo('pecl install mongo')
    php_add_extension('mongo.so')


@task
def install():
    fabd.mkdirs.run()

    php_install()
    php_zmq_install()
    php_redis_install()
    php_mongo_install()


@task
def setup():
    fabd.mkdirs.run()

    php_push_nginx_config.run()
    nginx.reload.run()


@task
def deploy():
    fabd.mkdirs.run()
    release.create.run()

    git.init.run()
    git.pull.run()

    run('mkdir --parent %(release_path)s/uploads/images' % env.conf)
    sudo('chmod 0777 %(release_path)s/uploads/images' % env.conf)

    release.activate.run()
