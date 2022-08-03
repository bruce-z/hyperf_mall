# Hypref Mall

#### 介绍
Hypref Mall 是一套开源的高性能微服务商城系统。高扩展、高性价比的企业级应用。


#### 软件架构
![输入图片说明](images/123.png)


#### 安装说明
##### 第一次安装会比较耗时，建议使用自带脚本工具进行安装，整个过程需要10-30分钟！！

    提前准备好Docker. 默认端口占用:5503-5508 5566-5568。

i. 自动安装(推荐)
   1. windows 下 运行install目录下的 hypref_mall_service.exe 命令``99``一键安装
   2. linux 下 执行 python ./main.py (python版本 > 3.0)
   
   安装后测试请求接口:http://127.0.0.1:5566/app/index/index 

ii. 手动安装

    1. 代码下载， 仓库地址：

            1. 路由层：https://gitee.com/scwlkj/hypref_mall_admin.git

            2. 图片API:https://gitee.com/scwlkj/hypref_mall_images.git

            3. 支付API：https://gitee.com/scwlkj/hypref_mall_pay.git

            4. 配置服务：https://gitee.com/scwlkj/hypref_mall_config.git

            5. 商品服务：https://gitee.com/scwlkj/hypref_mall_goods.git

            6. 订单服务:https://gitee.com/scwlkj/hypref_mall_order.git

            7. 会员服务:https://gitee.com/scwlkj/hypref_mall_member.git
        
        下载对应的项目代码    

    2. docker部署：

        其中：“D:\\project\\xxx\\xxx” 为本地项目路径 --name xxx 为 容器名

        命令：```docker run -v D:\\project\\xxx\\xxx:/data/project --name xxxx  -p 5566:5566 -it --privileged -u root --entrypoint /bin/sh         hyperf/hyperf:7.4-alpine-v3.11-swoole```


    3. 安装项目vendor扩展(相对比较耗时)

        进入容器的项目根目录下执行:composer install

    4. 初始化数据表

        sql脚本地址：项目下 -> static/SQL/sql.sql

    5. 修改env配置文件
       1. 修改数据库，填写自定义的数据库信息
       2. 修改redis信息
       3. 修改服务相关服务的IP和PORT.

    6. 启动所有服务


#### 使用说明

1.  基于Hypref框架 ，代码完全免费开源！


#### 特点

1.  简化微服务复杂的配置与调用过程，像开发单应用一样开发微服务系统！

2.  服务--一键生成基于数据表，对外提供的增删改查rpc服务.

3.  路由--一键生成服务的调用配置，让关注点聚焦业务.
