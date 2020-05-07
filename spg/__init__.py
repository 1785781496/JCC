'''
Spider Preferences Generator —— SPG
1、读取yaml
2、写入yaml
3、读取json
4、写入json
5、转换
6、从数据库读取
7、写入数据库
8、配置检查，一致性检查
9、配置验证verification，配置有效性验证


Spider Preferences Guide —— SPG
1、存储位置【多选】
    local: workfile
    net: publish
    other: source, render, etc.
2、项目 {project}
3、资产/镜头
4、资产类型 {asset_type}
5、集数/场次及关系
6、资产/镜头 {asset}/{shot}
7、环节 {step}
8、每种资产的pipeline
9、命名规范、大纲规范等
10、测试文件
11、配置生成
12、测试

WBS功能
    资产模板
        PR/P/AT/A/S
        PR/P/E/AT/A/S
        PR/P/SQ/AT/A/S
    镜头模板
        PR/P/SQ/ST/S
        PR/P/E/ST/S
        PR/P/E/SQ/ST/S
    剧集类
        PR/P/E/AT/A/S
        PR/P/E/SQ/ST/S
    电影类
        PR/P/AT/A/S
        PR/P/SQ/ST/S

    存储
        过程数据：分实体存储，两个实体关系
        结果数据：全路径，自动更新，使用的部分直接找最终结果
            关系调整后，重新计算，自动更新
        动态构建：动态调整

    逆向建立虚拟关系
        有了全部的AT/A/S和SQ/ST/S，可以直接归于一个P，也可以划分为P/E，所以是可转换的
        中间可以加入特定字段来满足客户的习惯，例如Asset/Shot等，可以用于管理，却不实际出现在路径上

    虚拟版本


'''