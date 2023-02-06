import json

from pyecharts import options as opts
from pyecharts.charts import Graph

with open("data/weibo2.json", "r", encoding="utf-8") as f:
    j = json.load(f)
nodes, links, categories, cont, mid, userl = j

g = (
    Graph()
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=50,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="微博转发关系图"),
    )
#     .render("微博转发关系图.html")
)
g.render()