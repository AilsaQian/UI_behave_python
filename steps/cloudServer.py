# -*- coding: UTF-8 -*-
from behave import *
from commonSteps import*
from nose.tools import assert_equals
from nose.tools import assert_not_equals
# from nose import tools
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@when(u'点击我的资产中云服务器，进入云服务器概览页')
def cosole_cloud(context):
    # switch_to_window(context, 1)
    find_elements_by_class_name(context, "chome_asset")[0].click()
    consoleTitle = find_element_by_class_name(context, "console_title").text
    assert_equals(consoleTitle, "云服务器概览")


@when(u'点击云服务器，点击概览，进入概览页')
def right_click_cloud(context):
    find_element_by_link_text(context, "云服务器").click()
    find_element_by_link_text(context, "概览").click()
    consoleTitle = find_element_by_class_name(context, "console_title").text
    assert_equals(consoleTitle, "云服务器概览")


@when(u'点击概览页元素{viewEle}，进入对应页面{viewPage}')
def check_cloudView_ele(context, viewEle, viewPage):
    if viewEle == "购买云服务器":
        find_element_by_class_name(context, "observer_add").click
        consoleTitle = find_element_by_class_name(context, "buy_head").text

    elif viewEle in ("云服务器", "云硬盘", "弹性IP", "镜像", "安全组", "快照", "密钥对", "更多监控指标"):
        if viewEle == "云服务器":
            find_element_by_class_name(
                context, "vpcView_pie_container").click()
        elif viewEle == "更多监控指标":
            find_element_by_class_name(
                context, "vpcView_info").click()
        elif viewEle == "云硬盘":
            find_element_by_xpath(
                context, "//a[@class='vpcView_disk']//p").click()
        elif viewEle == "弹性IP":
            find_element_by_xpath(
                context, "//a[@class='vpcView_floatIp']//p").click()
        elif viewEle == "镜像":
            find_element_by_xpath(
                context, "//a[@class='vpcView_image']//p").click()
        elif viewEle == "安全组":
            find_element_by_xpath(
                context, "//a[@class='vpcView_group']//p").click()
        elif viewEle == "快照":
            find_element_by_xpath(
                context, "//a[@class='vpcView_pic']//p").click()
        elif viewEle == "密钥对":
            find_element_by_xpath(
                context, "//a[@class='vpcView_key']//p").click()

        consoleTitle = find_element_by_class_name(
            context, "console_title").text

    assert_equals(consoleTitle, viewPage)


@when(u'选择主机{serverName}， 监控数据变为当前server的CPU使用率')
def server_Monitor(context, serverName):
    # ele = find_element_by_xpath(context, "//div[@class='vpcView_line']//h6")
    # logger.info(ele.getAttribute("innerHTML"))
    sleep(2)
    find_element_by_css_selector(
        context, ".serverSelectBox").click()
    # 切换选择给出的服务器
    find_element_by_xpath(
        context, "//ul[@class='selectBox_list']//li[contains(text(), '" + serverName + "')]").click()
    # find_elements_by_xpath(
    # context, "//ul[@class='selectBox_list']//li")[1].click()
    sleep(1)
    # 检查是否在监控所选云主机
    selectServerName = find_element_by_xpath(
        context, "//div[@class='vpcView_line']//h6").text
    assert_equals(selectServerName, serverName)


@then(u'进入监控页面，切换为同步类型{monitor}监控，展示不同主机{serverName}监控数据')
def server_monitor_diff_type(context, monitor, serverName):
    find_element_by_class_name(context, "vpcView_info").click()
    if monitor == "CPU使用率":
        find_elements_by_xpath(
            context, "//div[@class='vpcInfo_cont']//ul//li")[0].click()
    elif monitor == "带宽监控":
        find_elements_by_xpath(
            context, "//div[@class='vpcInfo_cont']//ul//li")[1].click()
    elif monitor == "系统盘监控":
        find_elements_by_xpath(
            context, "//div[@class='vpcInfo_cont']//ul//li")[2].click()
    activeTab = find_element_by_class_name(context, "vpcInfo_tab_active").text
    assert_equals(activeTab, monitor)


@when(u'点击云服务器，点击云服务器列表，进入云服务器列表页')
def server_list(context):
    find_element_by_link_text(context, "云服务器").click()
    find_element_by_link_text(context, "列表").click()
    consoleTitle = find_element_by_class_name(context, "console_title").text
    assert_equals(consoleTitle, "云服务器列表")


@when(u'查询服务器{serverName}，查询到对应信息')
def search_server(context, serverName):
    find_element_by_xpath(
        context, "//input[@placeholder='请输入云服务器名称查询']").send_keys(serverName)
    find_element_by_link_text(context, "查询").click()
    sleep(2)
    serverTitle = find_element_by_xpath(
        context, "//td[@class='server_name']//a").text
    assert_equals(serverTitle, serverName)


@when(u'点击服务器{serverName}，进入对应详情页面')
def server_list_detail(context, serverName):
    sleep(2)
    find_element_by_link_text(context, serverName).click()
    sleep(1)
    consoleTitle = find_element_by_class_name(context, "console_title").text
    server_Name = find_element_by_class_name(context, "vpcEdit_title").text[6:]
    assert_equals(consoleTitle, "云服务器详情")
    assert_equals(server_Name, serverName)


@when(u'点击云服务器，点击云硬盘，进入云硬盘列表页')
def server_disk(context):
    find_element_by_link_text(context, "云服务器").click()
    find_element_by_link_text(context, "云硬盘").click()
    consoleTitle = find_element_by_class_name(context, "console_title").text
    assert_equals(consoleTitle, "云硬盘")


@when(u'查询云硬盘{disk}，查询到对应信息')
def search_disk(context, disk):
    find_element_by_xpath(
        context, "//input[@placeholder='请输入云硬盘名称']").send_keys(disk)
    find_element_by_link_text(context, "查询").click()
    sleep(2)
    diskTitle = find_element_by_class_name(
        context, "console_td_warn_line").text
    assert_equals(diskTitle, disk)


@then(u'查看硬盘相关操作-购买、续费、挂载、卸载')
def oprate_disk(context):
    # 购买
    find_element_by_link_text(context, "购买云硬盘").click()
    modalName = find_element_by_xpath(
        context, "//div[@class='modal_head2']//h2").text
    assert_equals(modalName, "购买云硬盘")
    # 关闭小窗口
    find_element_by_class_name(context, "modal_close").click()
    # 续费
    find_element_by_class_name(context, "console_td_desc").click()
    modalName = find_element_by_xpath(
        context, "//div[@class='modal_head2']//h2").text
    assert_equals(modalName, "续费云硬盘")
    find_element_by_class_name(context, "modal_close").click()
    # 挂载
    # find_element_by_class_name(context, "console_td_more").click()
    # find_element_by_link_text(context, "挂载").click()


@when(u'点击云服务器，点击安全组，进入安全组列表页')
def server_security_group(context):
    find_element_by_link_text(context, "云服务器").click()
    find_element_by_link_text(context, "安全组").click()
    consoleTitle = find_element_by_class_name(context, "console_title").text
    assert_equals(consoleTitle, "安全组列表")


@when(u'查询安全组{securityGroup}，查询到对应信息')
def search_securityGroup(context, securityGroup):
    find_element_by_xpath(
        context, "//input[@placeholder='请输入安全组名称']").send_keys(securityGroup)
    find_element_by_link_text(context, "查询").click()
    sleep(2)
    groupTitle = find_elements_by_xpath(
        context, "//div[@class='console_list']//td")[0].text
    assert_equals(groupTitle, securityGroup)


@then(u'配置安全组规则，端口{port}，授权对象{remoteIP}')
def add_security_group_rule(context, port, remoteIP):
    find_element_by_link_text(context, "配置规则").click()
    find_element_by_xpath(
        context, "//div[@class='console_vpc_about']//button").click()
    # 填写端口范围和授权对象
    find_element_by_xpath(
        context, "//input[@reg='port_range']").send_keys(port)
    find_element_by_xpath(
        context, "//input[@reg='remote_ip_prefix']").send_keys(remoteIP)
    find_element_by_class_name(context, "modal_btnOk").click()
    # 检查提示
    sleep(2)
    warnText = find_element_by_class_name(context, "modal_warn").text
    assert_equals(warnText, "您好，您已经成功添加一条规则")
    find_element_by_class_name(context, "modal_btnHalf").click()
    # 检查列表中是否添加上
    portAdded = find_elements_by_xpath(context, "//tbody//td")[2].text
    assert_equals(portAdded, port)


@then(u'删除刚刚添加的安全组规则{port}')
def del_security_group_rule(context, port):
    find_elements_by_xpath(
        context, "//button[@class='console_td_del']")[0].click()
    find_element_by_class_name(context, "modal_btnOk").click()
    # 检查温馨提示
    sleep(2)
    warnText = find_element_by_class_name(context, "modal_warn").text
    assert_equals(warnText, "您好，您已经成功删除一条规则。")
    find_element_by_class_name(context, "modal_btnHalf").click()
    portValue = find_elements_by_xpath(context, "//tbody//td")[2].text
    assert_not_equals(portValue, port)
