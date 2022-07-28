import os
import platform
import threading

from past.types import basestring

import config
import time
import initDb


def init():
    # mysql服务
    task = threading.Thread(target=initMysql)
    task.start()

    # redis服务
    task = threading.Thread(target=initRedis)
    task.start()

    # 业务服务
    for service in config.services:
        task = threading.Thread(target=initService, args=(service,))
        task.start()


def initMysql():
    cc = os.popen("docker version")

    if not os.path.isdir(config.mysql_service['local_path']):
        os.makedirs(config.mysql_service['local_path'])
        print("\n创建目录： " + config.mysql_service['local_path'] + "\n")

    if 'Version' in cc.read():
        print("\n开始下载Mysql镜像 " + config.mysql_service['images'] + " \n")
        cc = os.popen("docker pull " + config.mysql_service['images'])
        if config.mysql_service['images'] in cc.read():
            print("\nMysql镜像下载完毕\n")
            run_string = "docker run -d --name " + config.mysql_service['service_name'] + " -v " + \
                         config.mysql_service['local_path'] + \
                         ":" + config.mysql_service['service_root'] + \
                         "  -e MYSQL_ROOT_PASSWORD=" + config.mysql_service['password'] + " -p " + \
                         str(config.mysql_service['port']) + ":3306  " + \
                         config.mysql_service['images']
            os.popen(run_string)
            print("\n Mysql服务 创建完毕 \n")


def initRedis():
    cc = os.popen("docker version")
    if 'Version' not in cc.read():
        print("\n docker命令未识别\n")
        return False

    print("\n开始下载redis镜像 " + config.redis_service['images'] + " \n")
    cc = os.popen("docker pull " + config.redis_service['images'] + ":latest")
    if config.redis_service['images'] in cc.read():
        print("\nredis镜像下载完毕\n")
        run_string = "docker run -d --name " + config.redis_service['service_name'] + " -p " + \
                     str(config.redis_service['port']) + ":6379  " \
                     + config.redis_service['images']
        os.popen(run_string)
        time.sleep(3)
        print("\n redis服务 创建完毕 \n")


def initService(service):
    path = config.base_dir + service['git_name']
    if not os.path.isdir(path):
        os.makedirs(path)
        print("\n创建目录： " + path + "\n")

    git_addr = config.git_pre + service['git_name'] + '.git'
    print("\n开始下载代码" + git_addr + "\n")

    aa = os.popen('git clone ' + git_addr + ' ' + path)
    if 'thisisjustnotifyend' not in aa.read():
        cc = os.popen("docker version")
        if 'Version' not in cc.read():
            print("\n docker命令未识别\n")
            return False

        print("\n开始下载镜像 " + config.docker_hypref_image + " \n")
        cc = os.popen("docker pull " + config.docker_hypref_image)
        if config.docker_hypref_image in cc.read():
            print("\n镜像下载完毕，开始创建容器：" + service['service_name'] + "\n")
            run_string = "docker run -v " + path + ":" + config.service_project_dir + " -p " \
                         + str(service['port']) + ":" + str(service['port']) + \
                         " --privileged -u root  " \
                         "--name " + service['service_name'] + " -dit " + config.docker_hypref_image
            ff = os.popen(run_string)
            if 'thisisjustnotifyend' not in ff.read():
                print("\n开始安装项目扩展\n")
                ee = os.popen('docker exec ' + service['service_name'] + ' bash -c "cd ' + config.service_project_dir
                              + '&& composer install" ')
                if 'thisisjustnotifyend' not in ee.read():
                    print("\n " + service['service_name'] + "扩展安装完成\n")

                    makeCopyCmd(path)
                    print("\n " + service['service_name'] + " env 文件已初始化，开始初始化数据库 ..\n")

                    if os.path.isfile(path + "/static/SQL/sql.sql"):
                        if isinstance(service['db_name'], basestring):
                            db = initDb.initDb(host='127.0.0.1', port=int(config.mysql_service['port']), user='root',
                                               password=config.mysql_service['password'], database=service['db_name'],
                                               filepath=path + "/static/SQL/sql.sql")
                            db.sql_run()
                    print("\n " + service['service_name'] + "数据库初始化完毕，重启服务中...\n")
                    reload_service(service['service_name'], service)


def makeCopyCmd(path):
    if platform.system().lower() != 'windows':
        # _cp = "cp"
        _de = "/"
    else:
        # _cp = "copy"
        _de = "\\"

    # return _cp + " " + path + _de + ".env.example " + path + _de + ".env"
    file = path + _de + ".env.example"
    file1 = path + _de + ".env"
    _data = ""
    with open(file, "r", encoding='UTF-8') as f:
        for line in f:
            if '127.0.0.1' in line:
                line = line.replace('127.0.0.1', config.local_ip)
            _data += line

    with open(file1, "w+", encoding='UTF-8') as w:
        w.write(_data)


def reload_service(name, service):
    try:
        ips = os.popen('docker exec ' + name + ' php ' + config.service_project_dir
                       + '/bin/hyperf.php start')
    finally:
        print("\n容器" + name + "服务已重启\n")
