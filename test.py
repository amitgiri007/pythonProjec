
import pandas as pd

s1 = [['FD', 302, 212121],
            ['FD', 596, 32434],
            ['FD', 530, 32342],
            ['FD', 612, 21233],
            ['PT', 5, 1233],
            ['PT', 14, 100],
            ['PT', 43, 1430],
            ['PT', 0O4, 213],
      ['WT', 5, 1233],
      ['WT', 39, 100],
      ['WT', 9, 1430],
      ['WT', 26, 213]
      ]
df = pd.DataFrame(s1,
                  columns=['PYMT_PRO', 'ERROR', 'CNT'])

print(df)

import holoviews as hv
from holoviews import opts, dim
import holoviews.plotting.bokeh
hv.extension('bokeh')
hv.output(size=200)

#add node labels
nodes = hv.Dataset(pd.DataFrame(df['PYMT_PRO']), 'index')
#create chord object
chord = hv.Chord((df, nodes)).select(value=(5, None))
#customization of chart
chord.opts(
           opts.Chord(cmap='Category20', edge_cmap='Category20',                              edge_color=dim('source').str(),
           labels='nodes', node_color=dim('index').str()))






