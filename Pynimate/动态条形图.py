# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 动态条形图
import matplotlib.pyplot as plt
import pandas as pd
import pynimate as nim
df = pd.DataFrame(
    {
        "time":["2020-01-01","2021-01-1","2022-01-01"],
        "Afghanistan":[1,2,3],
        "Angole":[2,3,4],
        "Albania":[1,2,5],
        "USA":[5,3,4],
        "Argentina":[1,4,5]
    }
).set_index("time")
cnv = nim.Canvas()
bar = nim.Barplot(df,"%Y-%m-%d","10d")
# bar.set_time(callback=lambda  i,datafier:datafier.data.index[i].year)
bar.set_time(callback=lambda i, datafier: datafier.data.index[i].strftime("%d  %b, %Y"))#时间标签
cnv.add_plot(bar)
cnv.animate()
cnv.save("file",24,"gif")
# cnv.save("file2",24,"mp4")
plt.show()

