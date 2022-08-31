import os
import threading
import config
import initProject

serviceName = [x['service_name'] for x in config.services]
ch_names = [x['ch_name'] for x in config.services]

serviceName.insert(0, 'all')
ch_names.insert(0, '全部服务')

string = ""
service_index = []
cmd_service = []
for index, name in enumerate(ch_names):
    if index % 2 == 1 and index > 0:
        string += "  " + str(index) + "： " + name + "\n\n"
    else:
        string += "  " + str(index) + "： " + name + "  |"

    index > 0 and cmd_service.append(str(index) + '1')
    service_index.append(str(index))

# 混淆判断字符串
mixString = "thisisjustnotifyend"


def reload_web_admin():
    service = config.web_admin
    path = config.base_dir + service['git_name']
    git_addr = config.git_pre + service['git_name'] + '.git'

    if not os.path.isdir(path):
        os.makedirs(path)
        print("\n创建目录： " + path + "\n")
        aa = os.popen('git clone ' + git_addr + ' ' + path)
    else:
        os.chdir(path)
        aa = os.popen('git pull ')

    print("\n开始下载代码" + path + "\n")

    if mixString not in aa.read():
        os.chdir(path)
        ee = os.popen('npm install --registry=https://registry.npm.taobao.org && npm run build:prod ')
        print("\n web_admin 代码初始化完成,开始build\n")
        if 'ERR' in ee.read():
            print("\n 项目构建失败，请重试!\n")
            return False

        if mixString not in ee.read():
            print("\n 构建成功!! 开始初始化运行环境\n")
            cc = os.popen("docker pull nginx")
            if mixString not in cc.read():
                ff = os.popen('docker build -t ' + service['images'] + ' ' + path)
                if mixString not in ff.read():
                    mm = os.popen('docker rm -f ' + service['images'])
                    if mixString not in mm.read():
                        print("\n " + service['images'] + "镜像已更新\n")
                        os.popen('docker run --name  ' + service['service_name'] + ' -d -p ' + str(service['port']) + ':80 '
                                 + service['images'])
                        print("\n web admin已启动\n")


def reload_service(name):
    if name == 'hypref_mall_font':
        reload_web_admin()
    else:
        try:
            ee = os.popen('docker exec ' + name + ' bash -c "cd ' + config.service_project_dir + '&& git pull" ')
            if 'notkissme' in ee:
                print("\n容器" + name + "git已pull\n")

            print("\n容器" + name + "关闭PHP进程...\n")
            os.system('docker start ' + name)
            os.system('docker exec ' + name + ' killall php')
            os.system('docker exec ' + name + ' php ' + config.service_project_dir + '/bin/hyperf.php start')
        finally:
            print("\n容器" + name + "服务已开始重启 ...\n")


def start_container():

    cm = input("  Hypref Mall 服务管理面板\n\n"
               + string +
               "\n\n-----------------------------\n\n"
               "    服务执行Hypref命令：服务编号后面+1\n"
               "    特殊命令 99->一键安装\n\n"
               "-----------------------------\n "
               "请输入要执行的命令编号：")

    if cm not in service_index:
        if cm in cmd_service:
            c = cm[0:1]
            mmm = input("输入命令,如：lazy:get config\n")
            if serviceName[int(c)] == 'hypref_mall_font':
                print("\nweb_admin不支持该命令\n")
            else:
                os.system('docker exec ' + serviceName[int(c)] + ' php ' + config.service_project_dir
                          + '/bin/hyperf.php ' + mmm)
        else:
            print("\n命令未识别，请输入正确的命令\n")
            start_container()
    elif cm == '99':
        nnn = input("确认开始初始化,Yes / No \n")
        if nnn == 'Yes' or nnn == 'yes':
            initProject.init()
        else:
            pass
        # start_container()
    else:
        name = serviceName[int(cm)]
        if name == 'all':
            for container_name in serviceName:
                if container_name != 'all':
                    task = threading.Thread(target=reload_service, args=(container_name,))
                    task.start()
        else:
            reload_service(name)
    start_container()


if __name__ == '__main__':
    start_container()
