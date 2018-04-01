from selenium import webdriver
import sys
from time import sleep
import imp
from infoConfig import USER_NAME, PASSWORD, BASE_SITE


def userLogin(context):
    context.browser.find_element_by_class_name("top_login").click()
    context.browser.find_element_by_link_text("账号登录").click()
    context.browser.find_element_by_xpath(
        "//input[@reg='user_name']").send_keys(USER_NAME)
    context.browser.find_element_by_xpath(
        "//input[@type='password']").send_keys(PASSWORD)
    context.browser.find_element_by_xpath("//input[@value='登录']").click()


def before_all(context):
    imp.reload(sys)
    # sys.setdefaultencoding('utf-8')
    context.browser = webdriver.Firefox()
    # 窗口最大化
    context.browser.maximize_window()
    # 打开网站
    baseUrl = BASE_SITE
    context.browser.get(baseUrl)
    # 用户登录
    userLogin(context)
    sleep(3)


def after_scenario(context, scenario):
    handles = context.browser.window_handles
    context.browser.switch_to_window(handles[0])
    handle = context.browser.current_window_handle
    for newhandle in handles:
        if newhandle != handle:
            context.browser.switch_to_window(newhandle)
            context.browser.close()
    context.browser.switch_to_window(handles[0])


def after_all(context):
    context.browser.quit()
