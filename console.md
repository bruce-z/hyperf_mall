### 管理工具介绍
  Hyperf mall 系统管理工具，实现一键初始化，快捷键重启hyperf服务、快捷键执行hyperf命令（Command）等。

### 启动工具
```python
 python3 ./main.py
```

### 常用命令介绍
- 0： 重启全部服务 

- 1-10 重启hyperf服务

- 1： 商品服务

- 2： 图片服务

- 3： 会员服务

- 4： 配置服务

- 5： 订单服务

- 6： 支付服务

- 7： 活动服务

- 8： 路由服务

- 9： 后台web_admin

- 10： pc端

  

- 97：单独安装 web_pc(商城pc端)

- 98: 单独安装 web_admin(商城管理后台)

- 99：一键安装系统

  

- 11：商品服务 hyperf command命令

- 31：会员服务 hyperf command命令

- 41：配置服务 hyperf command命令

- 51：订单服务 hyperf command命令

- 71：活动服务 hyperf command命令

- 81：路由服务 hyperf command命令



### 默认端口占用/通讯方式

- 商品服务 5503 RPC
-  图片服务 5504 HTTP
- 会员服务 5505 RPC
- 配置服务 5506 RPC
- 订单服务 5507 RPC
-  支付服务 5508 HTTP
-  活动服务 5509 RPC
-  路由服务 5566 HTTP
- Mysql数据库 5567 TCP
- Redis 5568 TCP
-  后台web_admin 5569 HTTP
-  pc端 5570 HTTP



### 重启步骤说明

1-8 （商品服务 - 路由服务）

> Step1: 启动容器（如果没有启动）
>
> Step2:  进入项目目录，更新项目代码，执行git pull 命令
>
> Step3: 关闭容器php进程 执行：killall php 命令
>
> Step4: 容器内执行hyperf启动命令: php ./hyperf.php start

后台web_admin、PC端重启步骤：

> Step1:  进入项目目录，如果不存在就自动创建并clone代码，如果存在就执行git pull 命令
>
> Step2: 执行npm install 安装新的node工具包
>
> Step3:执行 npm run build<xx> 打包项目
>
> Step4: 拉取镜像，如果不存在 docker pull nginx
>
> Step5: docker build -t 创建新的本地镜像
>
> Step6: 删除当前容器 docker rm -f
>
> Step7: docker run --name 创建并运行基于新镜像的容器



### 一键CURL命令说明

例如：orders模块下增加一个order_log表，实现常用的增删改查方法

启动工具后，执行命令：51，接着输入： lazy:get order_log

提示生成 

```
app/jsonRpc/OrderLogService.php # 对外的 rpc服务接口

app/jsonRpc/OrderLogService.php/OrderLogServiceInterface.php

app/Model/OrderLogModel.php

app/Repository/OrderLogRepository.php
```

执行命令：81，输入: lazy:get order_log orders

提示生成 

```
config/services/orders/OrderLogService.php

app/Service/Orders/OrderLogService.php

app/Service/Orders/Interfaces/OrderLogServiceInterfaces.php
```

至此生成可以直接调用的OrderLogService 默认提供方法：

```
* @method index(array $condition, array $field, int $page, int $size)
* @method update(int $id, array $data)
* @method delete(int $id)
* @method add(array $data)
* @method getRows(array $condition, array $field)
* @method getOne(array $condition, array $field = ['*'])
* @method appIndex(int $page, int $size)
   ```

基于某些原因，路由服务的前后端增删改查未做自动生成，需要根据业务实现校验后调用对应方法
