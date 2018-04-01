#language: zh-CN
功能: 检查首页页面元素

    场景大纲: 检查顶部页面元素
        当 点击顶部页面元素<topEle>，进入对应页面<topPage>
    例子:
        | topEle | topPage       |
        | 产品     | 产品中心PRODUCTS  |
        | 解决方案   | 金融解决方案        |
        | 技术支持   | 帮助与文档         |
        | 技术文档   | API支持SUPPORT  |
        | 关于我们   | 关于我们 ABOUT US |



    场景大纲: 检查滚动页面元素
        当 点击滚动页面<scrollBanner>，进入对应页面<scrollPage>
    例子:
        | scrollBanner | scrollPage |
        | dns          | 授权DNS      |
        | ddos         | 云防御IP      |
        | wsa          | 安全检测       |



    场景大纲: 检查产品推荐的了解详情
        当 点击推荐产品<hotPro>了解详情，进入对应详情页面
        当 点击咨询或者购买<hotPro>，进入工单页面或者购买页面<hotProBuyPage>
    例子:
        | hotPro | hotProBuyPage |
        | 授权DNS  | DNS           |
        | 云防御IP  | 云防御IP         |
        | 安全检测   | 安全检测          |



    场景大纲: 产品与解决方案
        当 点击行业<solutionItem>和了解详情，均进入对应详情页面<solutionPage>
    例子:
        | solutionItem | solutionPage |
        | 金融行业         | 金融解决方案       |
        | 企业门户         | 企业解决方案       |
        | 教育行业         | 教育解决方案       |
        | 游戏行业         | 游戏解决方案       |


    场景: 查看全部行业动态
        当 点击行业动态下面的查看全部，将进入行业动态页面


    场景大纲: 查看底部导航栏
        当 点击底部导航栏标签<footerItem>, 进入对应页面<footerPage>
    例子:
        | footerItem | footerPage   |
        | DNS        | 授权DNS        |
        | 云服务        | 定制云          |
        | 网络安全       | 域名安全         |
        | 融合通信       | 短信服务         |
        | 大数据        | 风险控制         |
        | 人工智能       | 机器学习平台       |
        | 常见故障       | 常见故障问题列表     |
        | 账号相关       | 账号相关         |
        | 销售相关       | 销售相关         |
        | API相关      | API相关        |
        | 公司简介       | 公司简介         |
        | 加入我们       | 招聘岗位         |
    #     # |服务条款||
    #     # |控制台||
    #     # |技术文档||
    #     # |帮助中心||
    #     # |攻击态势||
