#!/usr/bin/python
# -*- coding: windows-1250 -*-

import pandas as pd
import numpy as np

# nastavimo pogled za pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_html('http://www.worldgovernmentbonds.com/')[0].set_index('Country')

df['10Y Yield'] = [x.strip().replace(u'%', u'') for x in df['10Y Yield']]
df['10Y Yield'] = pd.to_numeric(df['10Y Yield'])

new_index = ['United States', 'Germany', 'Japan', 'China', 'India', 'Russia',
             'Brazil', 'Slovenia', 'Turkey', 'Mexico', 'Indonesia', 'Poland',
             'Italy', 'France', 'Australia', 'Spain', 'South Korea', 'United Kingdom']

df = df.reindex(new_index)
df.index.names = ['Država']
df.rename(columns={'10Y Yield': 'ObYTM'}, inplace=True)

df.reset_index(inplace=True)

preimenovanje = [(df['Država'] == 'United States'), (df['Država'] == 'Japan'), (df['Država'] == 'Slovenia'),
                 (df['Država'] == 'Germany'), (df['Država'] == 'Turkey'), (df['Država'] == 'Mexico'),
                 (df['Država'] == 'India'), (df['Država'] == 'Indonesia'), (df['Država'] == 'Italy'),
                 (df['Država'] == 'Russia'), (df['Država'] == 'China'), (df['Država'] == 'Brazil'),
                 (df['Država'] == 'Poland'), (df['Država'] == 'France'), (df['Država'] == 'Spain'),
                 (df['Država'] == 'United Kingdom'), (df['Država'] == 'Australia'), (df['Država'] == 'South Korea')]

izbira = ['ZDA', 'Japonska', 'Slovenija', 'Nemčija', 'Turčija', 'Mehika', 'Indija', 'Indonezija', 'Italija',
              'Rusija', 'Kitajska', 'Brazilija', 'Poljska', 'Francija', 'Španija', 'Velika Britanija', 'Avstralija',
              'Južna Koreja']

df['Država'] = np.select(preimenovanje, izbira)


df = df[['Država','ObYTM']]

print(df)