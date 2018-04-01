# -*- coding: UTF-8 -*-
from behave import *
from commonSteps import*
# from nose.tools import assert_equals
from nose import tools


@when(u'点击右侧导航栏的安全检测，进入安全检测页面')
def cosole_safe(context):
    switch_to_window(context, 1)
    # 先点击网络安全，出来了安全检测，再点击
    sleep(2)
    find_element_by_link_text(context, "网络安全").click()
    find_element_by_link_text(context, "安全检测").click()
    # 确定进入了安全监测页面
    consoleTitle = find_element_by_class_name(context, "console_title").text
    assert_equals(consoleTitle, "安全检测")


@when(u'点击添加域名按钮，添加域名{domain}和类型{type}')
def add_domain(context, domain, type):
    sleep(3)
    buttons = find_elements_by_xpath(
        context, "//div[@class='console_main']//button")
    # 如果第一次添加域名，button只有一个，但之后添加有多个，第二个是添加按钮
    if len(buttons) == 1:
        buttons[0].click()
    else:
        buttons[1].click()
    # 找到域名输入框
    domainText = find_element_by_xpath(
        context, "//div[@class='modal_verifyInput']/input")
    domainText.send_keys(domain)
    # 判断类型，是能成功添加的类型，还是重复添加，还是错误的域名
    if type in ("success", "duplication"):
        # 点击立即添加，添加域名
        sleep(1)
        find_element_by_class_name(context, "modal_btnOk").click()
        sleep(2)
        warningMsg = find_element_by_xpath(
            context, "//div[@class='modal_infoBody']//p//strong").text
        assert_equals(
            warningMsg, "在您要验证域名进行深度扫描时，请先在您的主机白名单里添加此116.211.142.1 /24 IP段")
        find_element_by_class_name(context, "modal_btnCancel").click()
    elif type == "failure":
        addButton = find_element_by_class_name(context, "modal_btnOk")
        styleButton = addButton.get_attribute("style")
        tools.assert_is_not_none(styleButton)
        # assert_equals(
        #     styleButton, "border-color: rgb(221, 221, 221);")


@then(u'点击添加域名按钮，再一次添加域名{domain}')
def add_domain_again(context, domain):
    sleep(2)
    buttons = find_elements_by_xpath(
        context, "//div[@class='console_main']//button")
    buttons[1].click()
    # 找到域名输入框
    domainText = find_element_by_xpath(
        context, "//div[@class='modal_verifyInput']/input")
    domainText.send_keys(domain)
    # 点击立即添加，添加域名
    sleep(1)
    find_element_by_class_name(context, "modal_btnOk").click()


@then(u'查看是否能添加成功{domain}')
def added(context, domain):
    # sleep(2)
    # context.browser.refresh()
    # sleep(1)
    domainList = find_elements_by_xpath(context, "//table//tbody//tr//td")
    domainName = domainList[0].text
    assert_equals(domainName, domain)


@then(u'提示添加域名错误{error}，点击取消')
def domain_add_errotr(context, error):
    errorMsg = find_element_by_class_name(context, "wsa_message").text
    assert_equals(errorMsg, error)
    find_element_by_class_name(context, "modal_btnCancel").click()


@then(u'删除已添加域名')
def delete_domain(context):
    # sleep(2)
    deleteList = find_elements_by_xpath(
        context, "//table//tbody//button[@class='console_td_del']")
    deleteList[0].click()
    # btnOk = find_element_by_class_name(context, "modal_btnOk")
    # sleep(1)
    # btnOk.click()
    find_element_by_class_name(context, "modal_btnOk").click()
