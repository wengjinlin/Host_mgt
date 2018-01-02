from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from bs_mgt import service as sc


service = sc.Service()


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        user = service.login(username, pwd)
        if user is not None:
            request.session['is_login'] = True
            request.session['login_user'] = user.nickname
            request.session['login_user_id'] = user.id
    return home(request)


def logout(request):
    request.session['is_login'] = False
    request.session['login_user'] = None
    request.session['login_user_id'] = None
    return redirect('/index')


def _host(request):
    DIRT = {}
    group_list = service.all_group()
    DIRT['group_list'] = group_list
    host_list = service.host_by_user(request.session['login_user_id'])
    DIRT['host_list'] = host_list
    return render(request, '_host.html', DIRT)


def _group(request):
    DIRT = {}
    group_list = service.all_group()
    DIRT['group_list'] = group_list
    return render(request, '_group.html', DIRT)


def home(request):
    if request.session.get('is_login', None) == True:
        DIRT = {'username': request.session['login_user']}
        return render(request, 'home.html', DIRT)
    else:
        return redirect('/index')


def del_host(request):
    # 删除指定主机
    user_id = request.session.get('login_user_id', None)
    host_id = request.GET.get('host_id', None)
    service.del_host(user_id, host_id)
    return redirect('/_host')


def add_host(request):
    # 添加主机修改主机
    host_id = request.POST.get('host_id', None)
    hostname = request.POST.get('hostname', None)
    ip = request.POST.get('ip', None)
    port = request.POST.get('port', None)
    os = request.POST.get('os', None)
    group = request.POST.get('hostgroup', None)
    data = [hostname, ip, port, os, group]
    user_id = request.session.get('login_user_id', None)
    if host_id is None or host_id =="":
        # 无传入id,为添加主机
        if service.add_check_data(data):
            service.add_host(user_id, data)
    else:
        # 有id，为修改主机
        if service.modify_check_data(host_id, data):
            service.modify_host(host_id, data)
    return redirect('/_host')


def del_group(request):
    # 删除分组
    if request.session.get('is_login', None) == True:
        group_id = request.GET.get('group_id', None)
        service.del_group(group_id)
    return redirect('/_group')


def add_group(request):
    # 添加修改分组
    if request.session.get('is_login', None) == True:
        groupname = request.POST.get('groupname', None)
        group_id = request.POST.get('group_id', None)
        if group_id is None or group_id == "":
            # 无传入id,为添加分组
            service.add_group(groupname)
        else:
            # 有传入id，为修改分组
            service.modify_group(group_id, groupname)
    return redirect('/_group')
