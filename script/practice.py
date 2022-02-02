# import json
# import os
#
# from pyecharts import options as opts
# from pyecharts.charts import Page, Tree
#
# data = [
#         {
#             "children": [
#                 {"name": "B"},
#                 {
#                     "children": [
#                         {"children": [{"name": "I"}], "name": "E"},
#                         {"name": "F"},
#                     ],
#                     "name": "C",
#                 },
#                 {
#                     "children": [
#                         {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
#                         {"name": "H"},
#                     ],
#                     "name": "D",
#                 },
#             ],
#             "name": "A",
#         }
#     ]
#
# tree=(
#      Tree()
#         .add("", data)
#         .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
#     )
#
# tree.render()
###
import re

line = "差异化重组中山集团>>端到端通道胡志明市业务群>>底层逻辑体系九江业务线>>如何收口集成济宁事业部>>" \
       "端到端横向西安交付部>>一致性迁移达拉斯团队>>结构化打法澳门界>>渗透兰州门>>资源倾斜维度淮安纲>>" \
       "感知度兰州目>>如何收口开拓柳州科>>WXG心力泉州属>>交付价值扩展驻马店种>>耦合性死磕秦皇岛甲>>" \
       "定性定量打透哈尔滨乙>>抽离透传合力丙>>价值转化吉隆坡丁>>WXG聚合马鞍山戊>>顶层设计长沙己>>精细化拆解肇庆庚"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# line = "a123b456b"
print(re.findall(r"(.+?)>>", line))
# 输出['123']#?控制只匹配0或1个,所以只会输出和最近的b之间的匹配情况

print(re.findall(r">>(.+)>>", line))
# 输出['123b456']

print(re.findall(r">>(.*)>>", line))
# 输出['123b456']


