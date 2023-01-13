import matplotlib.pyplot as plt
import sys
import math
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

fig, ax = plt.subplots( 3, 1, figsize=(9,18))
plt.subplots_adjust(left=0.1, bottom=0.07,  right=0.98, top=0.98, wspace=0.25, hspace=0.25)
#plt.subplots_adjust(left=0.1, bottom=0.07,  right=0.98, top=0.98)
#plt.tight_layout()

#x = [0,1,2,3]
#my_xticks = ['John','Arnold','Mavis','Matt']
#ax[0].set_xticks(x, my_xticks)
#ax[1].set_xticks(x, my_xticks)

ax[0].tick_params(axis='both', which='major', labelsize=35, direction = 'in', left = True, right = True, bottom = True, width = 1.5 , length = 10.0 )
ax[1].tick_params(axis='both', which='major', labelsize=35, direction = 'in', left = True, right = True, bottom = True, width = 1.5 , length = 10.0 )
ax[2].tick_params(axis='both', which='major', labelsize=35, direction = 'in', left = True, right = True, bottom = True, width = 1.5 , length = 10.0 )


ax[0].tick_params(axis='both', which='minor', labelsize=35, direction = 'in', left = True, right = True, bottom = True, width = 0.5 , length = 5.0 )
ax[1].tick_params(axis='both', which='minor', labelsize=35, direction = 'in', left = True, right = True, bottom = True, width = 0.5 , length = 5.0 )
ax[2].tick_params(axis='both', which='minor', labelsize=35, direction = 'in', left = True, right = True, bottom = True, width = 0.5 , length = 5.0 )


ax[0].set_xticks((0, 1, 2, 3, 4, 5))
ax[0].set_xticklabels((r'$\pi^{+}$', r'$\pi^{-}$', r'$K^{+}$', r'$K^{-}$', r'$p$', r'$\bar{p}$' ))

ax[1].set_xticks((0, 1, 2, 3, 4, 5))
ax[1].set_xticklabels((r'$\pi^{+}$', r'$\pi^{-}$', r'$K^{+}$', r'$K^{-}$', r'$p$', r'$\bar{p}$' ))

ax[2].set_xticks((0, 1, 2, 3, 4, 5))
ax[2].set_xticklabels((r'$\pi^{+}$', r'$\pi^{-}$', r'$K^{+}$', r'$K^{-}$', r'$p$', r'$\bar{p}$' ))

ax[0].set_xlim(-1.0,6.0)
ax[1].set_xlim(-1.0,6.0)
ax[2].set_xlim(-1.0,6.0)


#ax[ii,jj].set_yscale('linear')
ax[0].set_ylabel(r'$\frac{dN}{dy} (\vert y \vert < 0.1)$', fontsize = 25)
ax[1].set_ylabel(r'$\frac{dN}{dy} (\vert y \vert < 0.1)$', fontsize = 25)
ax[2].set_ylabel(r'$\frac{dN}{dy} (\vert y \vert < 0.1)$', fontsize = 25)
#ax[4,3].xaxis.set_visible(False)
#ax[0,1].yaxis.set_ticklabels([])
#ax[ii,jj].minorticks_on()
#ax[1,0].xaxis.set_minor_locator(MultipleLocator(10))
#ax[1,0].xaxis.set_minor_formatter('{x:.0f}')
#ax[ii,jj].tick_params(axis='both', which='major', labelsize=25, direction = 'in', left = True, right = True, bottom = True, width = 1.5 , length = 6.0 )

#ax[0,3].legend( fontsize = 15, frameon = False)
#ax[4,3].text(0.5, 0.11 , r'Au+Au @27 GeV', fontsize=30, color = 'black')
##ax[1,0].set_yticks([1, 3])

ax[0].set_yscale('log')
ax[1].set_yscale('log')
ax[2].set_yscale('log')

A1, B1, ERR1,LBB1,UBB1 = [],[],[],[],[]

COLOR = ['red', 'blue', 'limegreen']
LS = ['-','--','-.'] 
LABEL = [r'$\epsilon_f = 0.11$ GeV/fm$^3$',r'$\epsilon_f = 0.15$ GeV/fm$^3$',r'$\epsilon_f = 0.2$ GeV/fm$^3$']


#   =========  Au+Au 39 GeV ========  #
x = [0,1,2,3,4,5]
dndy = [182.3 , 185.8 , 32.0 , 25.0 , 26.5 , 8.5  ]
dndy_err = [20.1, 20.5, 2.9, 2.3, 2.9, 1.0]
ax[0].errorbar(x,dndy,yerr = dndy_err ,ms = 20,fmt="o",markeredgewidth = 4, markeredgecolor='black', markerfacecolor='white',color = 'black',elinewidth=5.4, alpha = 0.98, capsize = 6,label =r'STAR 0-5%')

FILE=[
'lower_mult_proxy_cut235.3upper_mult_proxy_cut1000.0eps_freeze_min0.11eps_freeze_max0.11epsilon_freeze0.11turn_on_baryon_diffusion1kappa_coefficient1.0/',
'lower_mult_proxy_cut235.3upper_mult_proxy_cut1000.0eps_freeze_min0.15eps_freeze_max0.15epsilon_freeze0.15turn_on_baryon_diffusion1kappa_coefficient1.0/',
'lower_mult_proxy_cut235.3upper_mult_proxy_cut1000.0eps_freeze_min0.2eps_freeze_max0.2epsilon_freeze0.2turn_on_baryon_diffusion1kappa_coefficient1.0/'
]
PART = [
'dndy_y-211_pT_0.01_3.dat',
'dndy_y--211_pT_0.01_3.dat',
'dndy_y-321_pT_0.01_3.dat',
'dndy_y--321_pT_0.01_3.dat',
'dndy_y-2212_pT_0.01_3.dat',
'dndy_y--2212_pT_0.01_3.dat',
] 




for ix in range(0,int(len(FILE))): 
  for iy in range(0,int(len(PART))): 
    FILE1 = FILE[ix] + PART[iy] 
    file1 = open(FILE1, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
      count += 1
      if count > 1 :
        values = [float(s) for s in line.split()]
        if(abs(values[0])<0.001) :
          A1.append(iy-0.3) 
          A1.append(iy+0.3)                                             
          B1.append(values[1]) 
          B1.append(values[1]) 
    if iy != 0 :
      ax[0].plot(A1, B1, ls = LS[ix], linewidth = 2.5, color = COLOR[ix])
    else :
      ax[0].plot(A1, B1, ls = LS[ix], linewidth = 2.5, color = COLOR[ix], label = LABEL[ix])

    A1.clear()
    B1.clear()
    ERR1.clear()
    LBB1.clear()
    UBB1.clear()






#   =========  Au+Au 19.6 GeV ========  #
x = [0,1,2,3,4,5]
dndy = [161.4, 165.8 , 29.6, 18.8 , 34.2 , 4.2   ]
dndy_err = [ 17.8, 18.3, 2.9, 1.9, 4.5, 0.5 ]
ax[1].errorbar(x,dndy,yerr = dndy_err ,ms = 20,fmt="o",markeredgewidth = 4, markeredgecolor='black', markerfacecolor='white',color = 'black',elinewidth=5.4, alpha = 0.98, capsize = 6,label =r'STAR 0-5%')

FILE=[
'lower_mult_proxy_cut215.7upper_mult_proxy_cut1000.0eps_freeze_min0.11eps_freeze_max0.11epsilon_freeze0.11turn_on_baryon_diffusion1kappa_coefficient1.0/',
'lower_mult_proxy_cut215.7upper_mult_proxy_cut1000.0eps_freeze_min0.15eps_freeze_max0.15epsilon_freeze0.15turn_on_baryon_diffusion1kappa_coefficient1.0/',
'lower_mult_proxy_cut215.7upper_mult_proxy_cut1000.0eps_freeze_min0.2eps_freeze_max0.2epsilon_freeze0.2turn_on_baryon_diffusion1kappa_coefficient1.0/'
]


PART = [
'dndy_y-211_pT_0.01_3.dat',
'dndy_y--211_pT_0.01_3.dat',
'dndy_y-321_pT_0.01_3.dat',
'dndy_y--321_pT_0.01_3.dat',
'dndy_y-2212_pT_0.01_3.dat',
'dndy_y--2212_pT_0.01_3.dat',
] 


for ix in range(0,int(len(FILE))): 
  for iy in range(0,int(len(PART))): 
    FILE1 = FILE[ix] + PART[iy] 
    file1 = open(FILE1, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
      count += 1
      if count > 1 :
        values = [float(s) for s in line.split()]
        if(abs(values[0])<0.001) :
          A1.append(iy-0.3) 
          A1.append(iy+0.3)                                             
          B1.append(values[1]) 
          B1.append(values[1]) 
    if iy != 0 :
      ax[1].plot(A1, B1, ls = LS[ix], linewidth = 2.5, color = COLOR[ix])
    else :
      ax[1].plot(A1, B1, ls = LS[ix], linewidth = 2.5, color = COLOR[ix], label = LABEL[ix])

    A1.clear()
    B1.clear()
    ERR1.clear()
    LBB1.clear()
    UBB1.clear()




#   =========  Au+Au 7.7 GeV ========  #
x = [0,1,2,3,4,5]
dndy = [93.4, 100 , 20.8, 7.7, 54.9 , 0.39  ]
dndy_err = [8.4 ,9.0, 1.7, 0.6, 6.1, 0.05]
ax[2].errorbar(x,dndy,yerr = dndy_err ,ms = 20,fmt="o",markeredgewidth = 4, markeredgecolor='black', markerfacecolor='white',color = 'black',elinewidth=5.4, alpha = 0.98, capsize = 6,label =r'STAR 0-5%')

FILE=[
'lower_mult_proxy_cut212.7upper_mult_proxy_cut1000.0eps_freeze_min0.11eps_freeze_max0.11epsilon_freeze0.11turn_on_baryon_diffusion1kappa_coefficient0.5/',
'lower_mult_proxy_cut212.7upper_mult_proxy_cut1000.0eps_freeze_min0.15eps_freeze_max0.15epsilon_freeze0.15turn_on_baryon_diffusion1kappa_coefficient0.5/',
'lower_mult_proxy_cut212.7upper_mult_proxy_cut1000.0eps_freeze_min0.2eps_freeze_max0.2epsilon_freeze0.2turn_on_baryon_diffusion1kappa_coefficient0.5/'
]
PART = [
'dndy_y-211_pT_0.01_3.dat',
'dndy_y--211_pT_0.01_3.dat',
'dndy_y-321_pT_0.01_3.dat',
'dndy_y--321_pT_0.01_3.dat',
'dndy_y-2212_pT_0.01_3.dat',
'dndy_y--2212_pT_0.01_3.dat',
] 


for ix in range(0,int(len(FILE))): 
  for iy in range(0,int(len(PART))): 
    FILE1 = FILE[ix] + PART[iy] 
    file1 = open(FILE1, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
      count += 1
      if count > 1 :
        values = [float(s) for s in line.split()]
        if(abs(values[0])<0.001) :
          A1.append(iy-0.3) 
          A1.append(iy+0.3)                                             
          B1.append(values[1]) 
          B1.append(values[1]) 
    if iy != 0 :
      ax[2].plot(A1, B1, ls = LS[ix], linewidth = 2.5, color = COLOR[ix])
    else :
      ax[2].plot(A1, B1, ls = LS[ix], linewidth = 2.5, color = COLOR[ix], label = LABEL[ix])

    A1.clear()
    B1.clear()
    ERR1.clear()
    LBB1.clear()
    UBB1.clear()







A100, B100 = [],[]
A100.append(0.3)
B100.append(0.11)
A100.append(0.5)
B100.append(0.11)


A200, B200 = [],[]
A200.append(-5)
B200.append(1)
A200.append(5)
B200.append(1)

#ax[0].plot(A100, B100, ls = '-', linewidth = 5.5, color = 'blue')

#ax[0].scatter(P1, R1, marker = 'o', s =10,  color = 'limegreen',facecolors='limegreen',linewidth = 2.5)

ax[0].text(-0.5, 10.11 , r'Au+Au @39 GeV', fontsize=30, color = 'grey')
ax[1].text(2.0, 100.11 , r'Au+Au @19.6 GeV', fontsize=30, color = 'grey')
ax[2].text(-0.8, 7.11 , r'Au+Au @7.7 GeV', fontsize=30, color = 'grey')

ax[0].legend( fontsize = 20, frameon = False)
ax[1].legend( fontsize = 20, frameon = False)
ax[2].legend( fontsize = 20, frameon = False)

plt.savefig('plot_particle_ratios.pdf', format = 'pdf', bbox_inches='tight')






