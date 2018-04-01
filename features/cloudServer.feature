#language: zh-CN
功能: 云服务器

    场景: 控制台进入云服务器
        当 点击控制台，进入用户中心
        当 点击我的资产中云服务器，进入云服务器概览页

    场景大纲: 检查云服务器概览
        当 点击控制台，进入用户中心
        当 点击云服务器，点击概览，进入概览页
        当 点击概览页元素<viewEle>，进入对应页面<viewPage>
    例子:
        | viewEle | viewPage |
        # | 购买云服务器  | 购买服务器     |
        | 云服务器 | 云服务器列表 |
        # | 更多监控指标  | 监控信息     |
        | 云硬盘  | 云硬盘    |
        | 弹性IP | 云服务器列表 |
        # | 镜像   | 镜像   |
        | 安全组 | 安全组列表 |
        # | 快照   |  快照   |
        # | 密钥对  |  密钥对  |

    场景大纲: 云服务器概览，切换主机，查看监控
        当 点击控制台，进入用户中心
        当 点击云服务器，点击概览，进入概览页
        # 当 点击购买云服务器，进入购买页
        当 选择主机<serverName>， 监控数据变为当前server的CPU使用率
        那么 进入监控页面，切换为同步类型<monitor>监控，展示不同主机<serverName>监控数据
    例子:
        | serverName | monitor |
        |短信回调测试服务器    | 系统盘监控   |
#
    场景大纲: 检查云服务器列表
        当 点击控制台，进入用户中心
        当 点击云服务器，点击云服务器列表，进入云服务器列表页
        当 查询服务器<serverName>，查询到对应信息
        当 点击服务器<serverName>，进入对应详情页面
    例子:
        | serverName |
        | 短信回调测试服务器  |

    # 场景大纲: 检查云服务器详情页 - 开关机
    #     当 点击控制台，进入用户中心
    #     当 点击云服务器，点击云服务器列表，进入云服务器列表页
    #     当 点击主机<cloudServer>，进入详情页面
    #     当 点击主机操作<cloudServerOpe>，状态变为<cloudServerStatus>
    # 例子:
    #     | cloudServer      | cloudServerOpe | cloudServerStatus |
    #     | testCloudServer1 | 开机             | 开机                |
    #     | testCloudServer2 | 关机             | 关机                |
    #     | testCloudServer3 | 休眠             | 休眠                |

    # 场景大纲: 检查云服务器详情页 - 页面跳转
    #     当 点击控制台，进入用户中心
    #     当 点击云服务器，点击云服务器列表，进入云服务器列表页
    #     当 点击主机<cloudServer>，进入详情页面
    #     当 点击跳转操作<cloudServerGoto>，进入对应页面<cloudServerGotoPage>
    # 例子:
    #     | cloudServer      | cloudServerGoto | cloudServerGotoPage |
    #     | testCloudServer1 | 续费              | 续费                  |
    #     | testCloudServer2 | 监控图表            | 监控图表                |
    #     | testCloudServer3 | 重置密码            | 重置密码                |

    场景大纲: 云硬盘列表
        当 点击控制台，进入用户中心
        当 点击云服务器，点击云硬盘，进入云硬盘列表页
        当 查询云硬盘<disk>，查询到对应信息
        那么 查看硬盘相关操作-购买、续费、挂载、卸载
    例子:
        |disk|
        |YYPJie|

    场景大纲: 安全组列表
        当 点击控制台，进入用户中心
        当 点击云服务器，点击安全组，进入安全组列表页
        当 查询安全组<securityGroup>，查询到对应信息
        那么 配置安全组规则，端口<port>，授权对象<remoteIP>
        那么 删除刚刚添加的安全组规则<port>
    例子:
        | securityGroup | port  | remoteIP |
        | fleio专用服务器    | 22/22 | 0.0.0.0  |

