"""This is the short example in the docs. Also edit the docs when you change
something here.

Below is an example of a short script to simulate groundwater levels
(the csv-files with the data can be found in the examples directory on GitHub)
"""

import pandas as pd

import pastas as ps

oseries = pd.read_csv('data/head_nb1.csv', parse_dates=['date'],
                      index_col='date', squeeze=True)
rain = pd.read_csv('data/rain_nb1.csv', parse_dates=['date'], index_col='date',
                   squeeze=True)
evap = pd.read_csv('data/evap_nb1.csv', parse_dates=['date'], index_col='date',
                   squeeze=True)

ml = ps.Model(oseries)
sm = ps.RechargeModel(prec=rain, evap=evap, rfunc=ps.Exponential,
                      recharge="Linear", name='recharge')
ml.add_stressmodel(sm)
ml.solve()
ml.plots.decomposition()
