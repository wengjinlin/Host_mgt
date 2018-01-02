# Host_mgt项目说明

> - 用Python3.0及以上解释器运行，运行环境保证编码为UTF-8，并配有Django环境
> - 需要在控制台中先运行两个命令：
>   - 1.python manage.py makemigrations
>   - 2.python magage.py migrate
> - 运行项目前需部署数据库：
>   - 1.自备数据库环境，并创建数据库（本项目默认采用mysql数据库，数据库名称为：host_mgt）
>   - 2.项目根目录/bs_mgt/service.py；修改该文件中Service类的构造方法，将ip,database,con修改以符合项目运行环境
>   - 3.如需要测试数据，运行->项目根目录/bs_mgt/createdata.py；运行前将该文件中的ip,database,con修改以符合项目运行环境
>   - 4.数据库表设计视图位置：项目根目录/Explain/DB/tables.jpg
> - 该项目为主机管理的后台管理系统，可对主机和分组信息进行管理，各用户拥有各自权限的主机，互不交叉，暂时将添加和删除分组信息的权限开放给所有用户
> - 具体各功能演示和测试用例见项目根目录/Explain/test.md