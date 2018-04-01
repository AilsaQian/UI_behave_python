# -*- coding: UTF-8 -*-
from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from nose.tools import assert_equals
from time import sleep


def switch_to_window(context, tab):
    context.browser.switch_to_window(context.browser.window_handles[tab])


def find_element_by_link_text(context, ele):
    linkTextElement = context.browser.find_element_by_link_text(ele)
    return linkTextElement


def find_element_by_class_name(context, ele):
    classNameElement = context.browser.find_element_by_class_name(ele)
    return classNameElement


def find_elements_by_class_name(context, ele):
    classNameElements = context.browser.find_elements_by_class_name(ele)
    return classNameElements


def find_element_by_xpath(context, ele):
    xpathElement = context.browser.find_element_by_xpath(ele)
    return xpathElement


def find_elements_by_xpath(context, ele):
    xpathElements = context.browser.find_elements_by_xpath(ele)
    return xpathElements


def find_element_by_css_selector(context, ele):
    xpathElement = context.browser.find_element_by_css_selector(ele)
    return xpathElement


def is_visible(context, locator, timeout=10):
    try:
        WebDriverWait(context.browser, timeout).until(
            EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False


@when(u'点击控制台，进入用户中心')
def console(context):
    # topLogin = find_element_by_xpath(context, "//div[@class='top_tool']//a")
    topLogin = find_element_by_class_name(context, "top_login")
    topLogin.click()
    # 因为点击控制台，会开启新窗口，句柄切换到下一个窗口
    switch_to_window(context, 1)
    sleep(2)
