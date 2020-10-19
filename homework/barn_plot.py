import numpy as np
import matplotlib.pyplot as plt
# plt.rc('text', usetex=True)
from scipy import interpolate

# 读取数据
u_235 = np.loadtxt('data/92-U-1.txt', skiprows=2)
u_238 = np.loadtxt('data/92-U-2.txt', skiprows=2)
h_1 = np.loadtxt('data/01-H-1_1.txt', skiprows=2)
o_16 = np.loadtxt('data/08-O-16.txt', skiprows=2)

# 处理U235，238数据
# 获取能量数据
x1 = u_235[:, 0]
y1 = u_235[:, 1]
# 截取不同能量点，获取不同能区
x11 = x1 > 1
x12 = x1 > 10000
x1_l_index = ~ x11
x1_m_index = x11 ^ x12
x1_h_index = x12
x1_l = x1[x1_l_index]
y1_l = y1[x1_l_index]
x1_m = x1[x1_m_index]
y1_m = y1[x1_m_index]
x1_h = x1[x1_h_index]
y1_h = y1[x1_h_index]
# print(y1_h)
# 处理U238数据
x2 = u_238[:, 0]
y2 = u_238[:, 1]
x21 = x2 > 1
x22 = x2 > 10000
x2_l_index = ~ x21
x2_m_index = x21 ^ x22
x2_h_index = x22
x2_l = x2[x2_l_index]
y2_l = y2[x2_l_index]
x2_m = x2[x2_m_index]
y2_m = y2[x2_m_index]
x2_h = x2[x2_h_index]
y2_h = y2[x2_h_index]

# 处理H，O数据
xh = h_1[:, 0]
yh = h_1[:, 1]
xo = o_16[:, 0]
yo = o_16[:, 1]
# 以H的能量点对O进行插值
f = interpolate.interp1d(xo, yo)    # 线性插值
yon = f(xh)
yn = 2 * yh + yon
# 取截面不平滑的部分
xhp_index = xh > 200000
xop_index = xo > 200000
xp = xh[xhp_index]
xop = xo[xop_index]
yhp = yh[xhp_index]
yop = yo[xop_index]
# fp = interpolate.interp1d(xop, yop)
# yonp = f(xp)
# yp = 2 * yhp + yonp
yp = yn[xhp_index]

# 绘制水中截面
fig, axs = plt.subplots(2, 1)
fig.suptitle('Section in water(' r'${\rm H_2O}$' '), ' r'${\rm ^1H}$' ', ' r'${\rm ^{16}O}$')
axs[0].loglog(xh, yn, label=r'${\rm H_2O}$')
axs[0].loglog(xh, yh, label=r'${\rm ^1H}$')
axs[0].loglog(xo, yo, label=r'${\rm ^{16}O}$')
axs[0].set_title('All energy neutron section in water(' r'${\rm H_2O}$' '), ' r'${\rm ^1H}$' ', ' r'${\rm ^{16}O}$')
axs[0].legend(prop={'size': 8})
axs[0].set_xlabel('Neutron Energy(eV)')
axs[0].set_ylabel('Section(b)')
axs[1].loglog(xp, yp, label=r'${\rm H_2O}$' ' part')
axs[1].loglog(xp, yhp, label=r'${\rm ^1H}$' ' part')
axs[1].loglog(xop, yop, label=r'${\rm ^{16}O}$' ' part')
axs[1].set_title('High energy neutron section in water(' r'${\rm H_2O}$' '), ' r'${\rm ^1H}$' ', 'r'${\rm ^{16}O}$')
axs[1].set_xlabel('Neutron Energy(eV)')
axs[1].set_ylabel('Section(b)')
axs[1].legend(prop={'size': 8})
plt.tight_layout()
# plt.show()
plt.savefig('Neutron section in water.png')
# xh2o = [xh == xo]
# print(xh, xo)
# exit(0)

# 绘制U235，U238截面
fig, axs = plt.subplots(2, 2)
fig.suptitle("Section in " r'${\rm ^{235}U}$' ", " r'${\rm ^{238}U}$')
axs[0, 0].loglog(x1_l, y1_l, color='blue', label=r'${\rm ^{235}U}$' '-Low_energy')
axs[0, 0].loglog(x2_l, y2_l, color='red', label=r'${\rm ^{238}U}$' '-Low_energy')
axs[0, 0].set_title("Low energy section")
axs[0, 0].set_xlabel('Energy/eV')
axs[0, 0].set_ylabel('Section/b')
axs[0, 1].loglog(x1_m, y1_m, color='yellow', label=r'${\rm ^{235}U}$' '-Middle_energy')
axs[0, 1].loglog(x2_m, y2_m, color='green', label=r'${\rm ^{238}U}$' '-Middle_energy')
axs[0, 1].set_title("Middle energy section")
axs[0, 1].set_xlabel('Energy/eV')
axs[0, 1].set_ylabel('Section/b')
axs[1, 0].plot(x1_h, y1_h, color='grey', label=r'${\rm ^{235}U}$' '-High_energy')
axs[1, 0].plot(x2_h, y2_h, color='pink', label=r'${\rm ^{238}U}$' '-High_energy')
axs[1, 0].set_title("High energy section")
# axs[1, 0].set_title(r'\TeX\ is Number $\sum_{n=1}^\infty' r'\frac{-e^{i\pi}}{2^n}$!', fontsize=16, color='r'))
axs[1, 0].set_xlabel('Energy/eV')
axs[1, 0].set_ylabel('Section/b')
fig.delaxes(axs[1, 1])
fig.legend(loc='upper left', bbox_to_anchor=(0.6, 0.4))
plt.tight_layout()
plt.savefig('Neutron section in U.png')
# plt.show()