import os
import threading
import initProject

serviceName = ['all', 'hypref_mall_member', 'hypref_mall_goods', 'hypref_mall_admin',
                'hypref_mall_images', 'hypref_mall_config', 'hypref_mall_pay']

#serviceName = ['all', 'member', 'goods', 'admin', 'images', 'config', 'orders', 'pay']


def reload_service(name):
    try:
        print("\n容器" + name + "关闭PHP进程...\n")
        os.system('docker start ' + name)
        os.system('docker exec ' + name + ' killall php')
        ips = os.system('docker exec ' + name + ' php /data/www/bin/hyperf.php start')
    finally:
        print("\n容器" + name + "服务已开始重启 ...\n")


def start_container():
    cm = input("  Hypref Mall 服务管理命令集成\n\n"
               "  1： 会员服务  |  2： 商品服务 \n\n"
               "  3： 路由服务  |  4： 图片服务 \n\n"
               "  5： 配置服务  |  6： 订单服务 \n\n"
               "  7： 支付服务  |  0： 全部服务 \n\n"
               "-----------------------------\n\n"
               "    服务脚本命令：编号后面+1\n" 
               "    例:会员服务命令 11\n"
               "    特殊命令 99->项目初始化\n\n"
               "-----------------------------\n "
               "请输入要执行的命令编号：")

    if cm not in ['0', '1', '2', '3', '4', '5', '6', '7', '99']:
        if cm in ['11', '21', '31', '41', '51', '61', '71']:
            c = cm[0:1]
            mmm = input("输入命令,如：lazy:get config\n")
            os.system('start /B docker exec ' + serviceName[int(c)] + ' php /data/www/bin/hyperf.php ' + mmm)
        else:
            print("\n请输入正确的命令\n")
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
