from bs_mgt import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_con():
    ip = "localhost"
    database = "host_mgt"
    con = "mysql+pymysql://root:@"+ip+"/"+database+"?charset=utf8"
    return con


# 创建表结构
engine = create_engine(db_con(), echo=True)
models.Base.metadata.create_all(engine)

# 添加初始数据
Session_class = sessionmaker(bind=engine)
Session = Session_class()
# # user
user1 = models.User(username='user1', password='123', nickname='sublime')
user2 = models.User(username='user2', password='123', nickname='alex')
# # host_group
g1 = models.Group(groupname='未分组')
g2 = models.Group(groupname='bbs')
g3 = models.Group(groupname='blog')
g4 = models.Group(groupname='portals')
# # host
h1 = models.Host(hostname='host1', ip='192.168.1.9', port='22', os='windows')
h2 = models.Host(hostname='host2', ip='192.168.1.10', port='22', os='windows')
h3 = models.Host(hostname='host3', ip='192.168.1.100', port='22', os='windows')
h4 = models.Host(hostname='host4', ip='192.168.1.56', port='22', os='windows')
h5 = models.Host(hostname='host5', ip='192.168.1.13', port='22', os='windows')
h6 = models.Host(hostname='host6', ip='192.168.2.10', port='55', os='linux')
h7 = models.Host(hostname='host7', ip='192.168.2.14', port='55', os='linux')
h8 = models.Host(hostname='host8', ip='192.168.2.23', port='55', os='linux')
h9 = models.Host(hostname='host9', ip='192.168.2.78', port='55', os='linux')
h10 = models.Host(hostname='host10', ip='192.168.3.101', port='9001', os='windows')
h11 = models.Host(hostname='host11', ip='192.168.3.15', port='9001', os='windows')
h12 = models.Host(hostname='host12', ip='192.168.3.84', port='9001', os='windows')
h13 = models.Host(hostname='host13', ip='192.168.3.64', port='9001', os='windows')
h14 = models.Host(hostname='host14', ip='192.168.3.32', port='9001', os='windows')
# # 建立关联关系
# ## 外键关联
user1.hosts = [h1, h2, h3, h4, h6, h7, h8, h11, h12, h14]
user2.hosts = [h5, h9, h10, h13]
g1.hosts = [h1, h5, h8, h11, h14]
g2.hosts = [h2, h3, h4]
g3.hosts = [h6, h7, h9]
g4.hosts = [h10, h12, h13]

Session.add_all([user1, user2, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, g1, g2, g3, g4])
Session.commit()
