import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Energy.xls', sheet_name=None, header=0)
sheet_1 = data['Sheet1'].replace('--', 0.0)
sheet_2 = data['Sheet2'].replace('--', 0.0)
plt.step(sheet_1['x1'], sheet_1['y1'], label='640', lw=0.2)
plt.step(sheet_1['x2'], sheet_1['y2'], label='240', lw=0.2)
plt.step(sheet_1['x3'], sheet_1['y3'], label='187', lw=0.2)
plt.step(sheet_1['x4'], sheet_1['y4'], label='175', lw=0.2)
plt.step(sheet_1['x5'], sheet_1['y5'], label='100', lw=0.2)
plt.plot(sheet_2['x'], sheet_2['y1'], '.-', label='', lw=0.2, ms=0.5)
plt.plot(sheet_2['x'], sheet_2['y2'], 'o-', label='', lw=0.2, ms=0.5)
plt.plot(sheet_2['x'], sheet_2['y3'], 'v-', label='', lw=0.2, ms=0.5)
plt.xscale('log')
plt.xlabel('Energy(eV)')
plt.ylim((0, 5))
plt.ylabel('')
plt.legend()
plt.savefig('plot.pdf')
#plt.show()
#print(data['Sheet1'])
