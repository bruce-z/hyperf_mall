# -*-coding:utf-8-*-

"""
 初始化安装配置文件
  - 不熟悉时安装流程时 不用修改任何配置信息
  - 确保端口不会被占用 -- 如果占用 需修改对应服务端口
"""

import platform

# git仓库前缀配置 不可修改
import socket

git_pre = 'https://gitee.com/scwlkj/'

# 本地项目路径配置
if platform.system().lower() == 'windows':
    base_dir = "D:\\project\\hypref_mall2\\"
else:
    base_dir = "/www/hypref_mall/"

# Hypref镜像版本配置
docker_hypref_image = "hyperf/hyperf:7.4-alpine-v3.11-swoole"

# docker容器内项目路径配置 一般默认不需要改动
service_project_dir = "/data/www"

# 服务配置
services = [
    {
        'git_name': 'hypref_mall_goods',  # git仓库名字 不可修改 -- 商品服务
        'service_name': 'hyperf_mall_goods',  # 服务名，默认与仓库名保持一致， 可自定义
        'ch_name': '商品服务',
        'port': 5503,  # 启用端口 默认 本地与 docker启动 端口一致，可自定义
        'db_name': 'goods',  # 数据库名字
    },
    {
        'git_name': 'hypref_mall_images',  # git仓库名字 不可修改 -- 图片服务
        'service_name': 'hyperf_mall_images',
        'ch_name': '图片服务',
        'port': 5504,
        'db_name': 'file_center',
    },
    {
        'git_name': 'hypref_mall_member',  # git仓库名字 不可修改 -- 会员服务
        'service_name': 'hyperf_mall_member',
        'ch_name': '会员服务',
        'port': 5505,
        'db_name': 'member',
    },
    {
        'git_name': 'hypref_mall_config',  # git仓库名字 不可修改 -- 配置服务
        'service_name': 'hyperf_mall_config',
        'ch_name': '配置服务',
        'port': 5506,
        'db_name': 'config',
    },
    {
        'git_name': 'hypref_mall_order',  # git仓库名字 不可修改 -- 订单服务
        'service_name': 'hyperf_mall_order',
        'ch_name': '订单服务',
        'port': 5507,
        'db_name': 'orders',
    },
    {
        'git_name': 'hypref_mall_pay',  # git仓库名字 不可修改 -- 支付服务
        'service_name': 'hyperf_mall_pay',
        'ch_name': '支付服务',
        'port': 5508,
        'db_name': False,
    },
    {
        'git_name': 'hyperf_mall_activity',  # git仓库名字 不可修改 -- 支付服务
        'service_name': 'hyperf_mall_activity',
        'ch_name': '活动服务',
        'port': 5509,
        'db_name': False,
    },
    {
        'git_name': 'hypref_mall_admin',  # git仓库名字 不可修改 -- 路由服务
        'service_name': 'hyperf_mall_admin',
        'ch_name': '路由服务',
        'port': 5566,
        'db_name': False,
    },
    {
        'git_name': 'hypref_mall_font',  # git仓库名字 不可修改 -- 后台web站点
        'service_name': 'hyperf_mall_font',  # 名字被占用，如需修改，需要修改main.py中对应的值
        'ch_name': '后台web_admin',
        'port': 5569,
        'db_name': False,
    },
]

# 数据库服务
mysql_service = {
    'images': "mysql:5.7.37",
    'service_name': 'hyperf_mall_mysql',
    'port': 5567,
    'local_path': base_dir + '/mysql/data',
    'service_root': '/var/lib/mysql',
    'password': 'root123'
}
# redis服务
redis_service = {
    'images': "redis",
    'service_name': 'hyperf_mall_redis',
    'port': 5568
}

# web-admin 后台
web_admin = {
    'git_name': "hypref_mall_font",
    'images': "hyperf_mall_font",
    'service_name': 'hyperf_mall_font',
    'port': 5569
}

# 获取当前IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
