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


def reload_service(name):
    try:
        print("\n容器" + name + "关闭PHP进程...\n")
        os.system('docker start ' + name)
        os.system('docker exec ' + name + ' killall php')
        os.system('docker exec ' + name + ' php ' + config.service_project_dir + '/bin/hyperf.php start')
    finally:
        print("\n容器" + name + "服务已开始重启 ...\n")


def start_container():

    cm = input("  Hypref Mall 服务管理命令集成\n\n"
               + string +
               "-----------------------------\n\n"
               "    服务脚本命令：编号后面+1\n"
               "    例:会员服务命令 11\n"
               "    特殊命令 99->一键安装\n\n"
               "-----------------------------\n "
               "请输入要执行的命令编号：")

    if cm not in service_index:
        if cm in cmd_service:
            c = cm[0:1]
            mmm = input("输入命令,如：lazy:get config\n")
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
