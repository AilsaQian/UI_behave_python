# -*- coding: UTF-8 -*-
from behave import *
from nose.tools import assert_equals
from time import sleep
from selenium.webdriver.common.by import By
from commonSteps import*
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@when(u'点击顶部页面元素{topEle}，进入对应页面{topPage}')
def verify_top_tab(context, topEle, topPage):
    # 获取顶部标签，并点击进入对应页面
    find_element_by_link_text(context, topEle).click()
    # 不同页面标志文本，目前首页和技术文档sidebar_head标记，关于我们是sidebar_title
    if topEle in ['产品', '技术文档']:
        headText = find_element_by_class_name(context, "sidebar_head").text
    elif topEle == '关于我们':
        headText = find_element_by_class_name(context, "sidebar-title").text
    elif topEle == '解决方案':
        headText = find_element_by_xpath(
            context, "//div[@class='resBanner_cont']/h1").text
    elif topEle == '技术支持':
        headText = find_element_by_class_name(
            context, "site-header__title").text
    assert_equals(headText, topPage)


@when(u'点击滚动页面{scrollBanner}，进入对应页面{scrollPage}')
def verify_scollBanner(context, scrollBanner, scrollPage):
    # 回到首页
    find_element_by_class_name(context, "top_logo").click()
    # sleep(2)
    if scrollBanner == 'dns':
        locator = (By.CLASS_NAME, "banner_item1")
        bannerItem = find_element_by_class_name(context, "banner_item1")
    elif scrollBanner == 'ndc':
        locator = (By.CLASS_NAME, "banner_item2")
        bannerItem = find_element_by_class_name(context, "banner_item2")
    elif scrollBanner == 'ddos':
        locator = (By.CLASS_NAME, "banner_item3")
        bannerItem = find_element_by_class_name(context, "banner_item3")
    elif scrollBanner == 'wsa':
        locator = (By.CLASS_NAME, "banner_item4")
        bannerItem = find_element_by_class_name(context, "banner_item4")
    # 等待元素出现
    is_visible(context, locator)
    # 进入产品详情页
    bannerItem.click()
    sleep(1)
    # 窗口句柄跳到当前页面
    switch_to_window(context, 1)
    productDesc = find_element_by_xpath(
        context, "//div[@class='product_banner']//h2").text
    assert_equals(productDesc, scrollPage)


@when(u'点击推荐产品{hotPro}了解详情，进入对应详情页面')
def verify_hotPro_detail(context, hotPro):
    # 回到首页
    find_element_by_class_name(context, "top_logo").click()
    sleep(1)
    hotProDetailItems = find_elements_by_class_name(
        context, "hotProduct_info")
    if hotPro == '授权DNS':
        hotProDetailItems[0].click()
    elif hotPro == '云防御IP':
        hotProDetailItems[2].click()
    elif hotPro == '安全检测':
        hotProDetailItems[3].click()

    sleep(2)
    switch_to_window(context, 1)
    productDesc = find_element_by_xpath(
        context, "//div[@class='product_banner']//h2").text
    assert_equals(productDesc, hotPro)


@when(u'点击咨询或者购买{hotPro}，进入工单页面或者购买页面{hotProBuyPage}')
def verify_hotPro_Buy(context, hotPro, hotProBuyPage):
    # 回到首页
    find_element_by_class_name(context, "top_logo").click()
    sleep(1)
    hotProBuyItems = find_elements_by_class_name(
        context, "hotProduct_buy")
    if hotPro == '授权DNS':
        hotProBuyItems[0].click()
        sleep(2)
        switch_to_window(context, 2)
        hotProBuy = find_element_by_class_name(context, "buy_head").text
    elif hotPro == '云防御IP':
        hotProBuyItems[2].click()
        hotProBuy = find_element_by_class_name(context, "buy_head").text
    elif hotPro == '安全检测':
        hotProBuyItems[3].click()
        hotProBuy = find_element_by_xpath(
            context, "//div[@class='product_banner']//h2").text

    # hotProBuy = find_element_by_class_name(context, "buy_head")
    assert_equals(hotProBuy, hotProBuyPage)


@when(u'点击行业{solutionItem}和了解详情，均进入对应详情页面{solutionPage}')
def solution(context, solutionItem, solutionPage):
    if solutionItem == '金融行业':
        solutionBg = find_element_by_class_name(
            context, "solution_mainBg1")
        # 找到了解详情元素
        # solutionLink = find_element_by_xpath(
        #     context,
        #     "//section[@class='solution']//a[@href='/resolve/finance']/a[@class='solution_link']")
        # locator = (
        #     By.XPATH,
        #     "//section[@class='solution']//a[@href='/resolve/finance']/a[@class='solution_link']")
    elif solutionItem == '企业门户':
        solutionBg = find_element_by_class_name(
            context, "solution_mainBg2")
    elif solutionItem == '教育行业':
        solutionBg = find_element_by_class_name(
            context, "solution_mainBg3")
    elif solutionItem == '游戏行业':
        solutionBg = find_element_by_class_name(
            context, "solution_mainBg4")
    # 获取解决方案元素，点击进入解决方案详情页
    solutionBg.click()
    sleep(3)
    switch_to_window(context, 1)
    headText = find_element_by_xpath(
        context, "//div[@class='resBanner_cont']/h1").text
    assert_equals(headText, solutionPage)

    # # 点击首页，回到首页，然后点击了解详情
    # find_element_by_link_text(context, "首页").click()
    # # time.slepp(3)
    # is_visible(context, locator)
    # solutionLink.click()
    # # sleep(3)
    # switch_to_window(context, 1)
    # headText = find_element_by_xpath(
    #     context, "//div[@class='resBanner_cont']/h1").text
    # assert_equals(headText, "")


@when(u'点击行业动态下面的查看全部，将进入行业动态页面')
def check_news(context):
    find_element_by_link_text(context, "查看全部").click()
    # sleep(1)
    switch_to_window(context, 1)
    sleep(3)
    newsPage = find_elements_by_xpath(
        context, "//span[@itemprop='name']")[1].text
    assert_equals(newsPage, "行业动态")


@when(u'点击底部导航栏标签{footerItem}, 进入对应页面{footerPage}')
def footer_page(context, footerItem, footerPage):
    xpathEle = "//ul[@class='footer_list']//a[text()='" + footerItem + "']"
    find_element_by_xpath(
        context, xpathEle).click()
    switch_to_window(context, 1)
    sleep(1)

    if footerItem in ['解析入门', '功能介绍', '常见故障', '账号相关', '销售相关', 'API相关']:
        # sleep(3)
        # 因为解析入门页面打开太慢，所以等帮助与文档显示出来之后再捕捉想捕捉的元素
        locator = (By.CLASS_NAME, "mysite-header__title")
        is_visible(context, locator)
        # switch_to_window(context, 1)
        footerPageHeader = find_elements_by_xpath(
            context, "//span[@itemprop='name']")[1].text
    elif footerItem in ['公司简介', '加入我们', '联系我们']:
        # switch_to_window(context, 1)
        footerPageHeader = find_element_by_xpath(
            context, "//div[@class='comm-cont']//h4").text
    else:
        # switch_to_window(context, 1)
        footerPageHeader = find_element_by_xpath(
            context, "//div[@class='product_banner']//h2").text
    assert_equals(footerPageHeader, footerPage)
