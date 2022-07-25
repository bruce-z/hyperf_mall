# Hypref Mall

#### 介绍
Hypref Mall 是一套开源的高性能微服务商城系统，高扩展性，高性价比的企业级应用。


初始化脚本暂未编写...(2022/07/25)


#### 软件架构
![输入图片说明](123.png)


#### 安装说明
##### 第一次安装会比较耗时，建议使用自带脚本工具进行安装，整个过程需要10-30分钟！！

1.  提前准备好Docker、Python3、MySQL、Redis。

2.  代码下载

    仓库地址：

            1. 路由层：git@gitee.com:scwlkj/hypref_mall_admin.git

            2. 图片API:git@gitee.com:scwlkj/hypref_mall_images.git

            3. 支付API：git@gitee.com:scwlkj/hypref_mall_pay.git

            4. 配置服务：git@gitee.com:scwlkj/hypref_mall_config.git

            5. 商品服务：git@gitee.com:scwlkj/hypref_mall_goods.git

            6. 订单服务:git@gitee.com:scwlkj/hypref_mall_order.git

            7、会员服务:git@gitee.com:scwlkj/hypref_mall_member.git

            8、uniapp端 生成小程序

            9、admin后台管理

    或者：进入到安装目录后执行一键下载脚本 ./install.py


3.  初始化DB信息，执行 ./initDb.py


4.  docker部署：

    其中：“D:\\project\\xxx\\xxx” 为本地项目路径

    命令：```docker run -v D:\\project\\xxx\\xxx:/data/project --name admin  -p 5566:5566 -it --privileged -u root --entrypoint /bin/sh hyperf/hyperf:7.4-alpine-v3.11-swoole```


    执行 ./initDocker.py 一键生成 docker容器

5.  服务compoer安装vendor扩展(可能会比较耗时)

    执行 ./initVendor.py 一键安装 或者进入单个容器中，进入项目目录下:composer install


6.  修改项目下env配置文件，或者执行 ./initEnv.py 一键修改


7.  执行 hypref_mall_service.exe 根据命令一键启动所有服务


#### 使用说明

1.  基于Hypref框架 ，代码完全免费开源！


#### 特点

1.  简化微服务复杂的配置与调用过程，像开发单应用一样开发微服务系统！

2.  封装很多提升开发速度的工具，服务端一键生成对外初始增删改查的服务RPC，路由层一键生成微服务的各项配置...
