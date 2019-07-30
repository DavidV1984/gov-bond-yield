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
df.index.names = ['Dr�ava']
df.rename(columns={'10Y Yield': 'ObYTM'}, inplace=True)

df.reset_index(inplace=True)

preimenovanje = [(df['Dr�ava'] == 'United States'), (df['Dr�ava'] == 'Japan'), (df['Dr�ava'] == 'Slovenia'),
                 (df['Dr�ava'] == 'Germany'), (df['Dr�ava'] == 'Turkey'), (df['Dr�ava'] == 'Mexico'),
                 (df['Dr�ava'] == 'India'), (df['Dr�ava'] == 'Indonesia'), (df['Dr�ava'] == 'Italy'),
                 (df['Dr�ava'] == 'Russia'), (df['Dr�ava'] == 'China'), (df['Dr�ava'] == 'Brazil'),
                 (df['Dr�ava'] == 'Poland'), (df['Dr�ava'] == 'France'), (df['Dr�ava'] == 'Spain'),
                 (df['Dr�ava'] == 'United Kingdom'), (df['Dr�ava'] == 'Australia'), (df['Dr�ava'] == 'South Korea')]

izbira = ['ZDA', 'Japonska', 'Slovenija', 'Nem�ija', 'Tur�ija', 'Mehika', 'Indija', 'Indonezija', 'Italija',
              'Rusija', 'Kitajska', 'Brazilija', 'Poljska', 'Francija', '�panija', 'Velika Britanija', 'Avstralija',
              'Ju�na Koreja']

df['Dr�ava'] = np.select(preimenovanje, izbira)


df = df[['Dr�ava','ObYTM']]

print(df)