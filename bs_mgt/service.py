from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from bs_mgt import models
import re


class Service(object):
    def __init__(self):
        ip = "localhost"
        database = "host_mgt"
        con = "mysql+pymysql://root:@" + ip + "/" + database + "?charset=utf8"
        engine = create_engine(con, echo=False)
        Session_class = sessionmaker(bind=engine)
        self.Session = Session_class()

    def login(self, username, password):
        # 验证用户登录
        user = self.Session.query(models.User).filter(models.User.username == username).first()
        if user is not None and password == user.password:
            return user
        return None

    def all_group(self):
        # 获取所有分组信息
        group_list = self.Session.query(models.Group).all()
        return group_list

    def group_by_id(self, group_id):
        # 获取指定分组
        group = self.Session.query(models.Group).filter(models.Group.id == group_id).first()
        return group

    def group_by_name(self, groupname):
        # 获取指定主机
        group = self.Session.query(models.Group).filter(models.Group.groupname == groupname).first()
        return group

    def ungrouped(self):
        # 返回默认分组--未分组
        group = self.Session.query(models.Group).filter(models.Group.groupname == "未分组").first()
        return group

    def host_by_user(self, user_id):
        # 获取用户管理主机
        host_list = self.Session.query(models.Host).filter(models.Host.user_id == user_id).all()
        return host_list

    def del_host(self, user_id, host_id):
        # 删除用户权限范围内的指定主机
        host = self.host_by_id(host_id)
        if host is not None:
            if host.user_id == user_id:
                self.Session.delete(host)
                self.Session.commit()

    def host_by_id(self, host_id):
        # 获取指定主机
        host = self.Session.query(models.Host).filter(models.Host.id == host_id).first()
        return host

    def host_by_ip(self, ip):
        # 获取指定主机
        host = self.Session.query(models.Host).filter(models.Host.ip == ip).first()
        return host

    def host_by_name(self, host_name):
        # 获取指定主机
        host = self.Session.query(models.Host).filter(models.Host.hostname == host_name).first()
        return host

    def add_check_data(self, data):
        # 添加host数据验证
        flag = True
        hostname = data[0]
        ip = data[1]
        port = data[2]
        os = data[3]
        group = data[4]
        group_list = []
        m = re.match(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b', ip)
        if self.host_by_name(hostname) is not None:
            # hostname不能重复
            flag = False
        if m is None and self.host_by_ip(ip) is None:
            # IP格式检查，且不能重复
            flag = False
        try:
            int(port)
        except:
            # 端口为数字
            flag = False
        if os != "windows" and os != 'linux':
            # 只能匹配这两个系统
            flag = False
        for g in self.all_group():
            group_list.append(g.groupname)
        if group not in group_list:
            # 只能匹配已创建的group
            flag = False
        return flag

    def modify_check_data(self, host_id, data):
        # 修改host数据验证
        flag = True
        hostname = data[0]
        ip = data[1]
        port = data[2]
        os = data[3]
        group = data[4]
        group_list = []
        m = re.match(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b', ip)
        host = self.host_by_name(hostname)
        if host is not None and str(host.id) != host_id:
            # 修改后hostname重复
            # print("hostname wrong")
            flag = False
        if m is None:
            # IP格式错误
            # print("ip wrong 1")
            flag = False
        else:
            host = self.host_by_ip(ip)
            if host is not None and str(host.id) != host_id:
                # 修改后ip重复
                # print("ip wrong 2")
                flag = False
        try:
            int(port)
        except:
            # 端口为数字
            # print("port wrong")
            flag = False
        if os != "windows" and os != 'linux':
            # 只能匹配这两个系统
            # print("os wrong")
            flag = False
        for g in self.all_group():
            group_list.append(g.groupname)
        if group not in group_list:
            # 只能匹配已创建的group
            # print("group wrong")
            flag = False
        return flag

    def add_host(self, user_id, data):
        # 添加主机
        host = models.Host(hostname=data[0], ip=data[1], port=data[2], os=data[3])
        user = self.Session.query(models.User).filter(models.User.id == user_id).first()
        group = self.Session.query(models.Group).filter(models.Group.groupname == data[4]).first()
        host.user = user
        host.host_group = group
        self.Session.add(host)
        self.Session.commit()

    def modify_host(self, host_id, data):
        # 修改主机
        host = self.Session.query(models.Host).filter(models.Host.id == host_id).first()
        host.hostname = data[0]
        host.ip = data[1]
        host.port = data[2]
        host.os = data[3]
        group = self.Session.query(models.Group).filter(models.Group.groupname == data[4]).first()
        host.host_group = group
        self.Session.commit()

    def del_group(self, group_id):
        # 删除分组，并将该分组下的所有主机分配到默认分组中
        group = self.group_by_id(group_id)
        d_group = self.ungrouped()
        h_list = group.hosts
        # print(h_list)
        if group is not None:
            if group.id != d_group.id:
                # print(len(h_list))
                for host in h_list[:]:
                    # print(host.id)
                    # print(host)
                    # print(host.host_group)
                    # print(type(host.host_group))
                    host.host_group = d_group
                    self.Session.commit()
                    # print(h_list)
                self.Session.delete(group)
                self.Session.commit()

    def add_group(self, groupname):
        # 添加分组
        if self.group_by_name(groupname) is None:
            group = models.Group(groupname=groupname)
            self.Session.add(group)
            self.Session.commit()

    def modify_group(self, group_id, groupname):
        # 修改分组
        group = self.group_by_name(groupname)
        g = self.group_by_id(group_id)
        if group is None:
            g.groupname = groupname
            self.Session.commit()
