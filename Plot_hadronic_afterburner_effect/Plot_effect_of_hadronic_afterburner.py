import matplotlib.pyplot as plt
import sys
import math
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


fig, ax = plt.subplots( 6, 4, figsize=(24,20))
#plt.subplots_adjust(left=0.1, bottom=0.07,  right=0.98, top=0.98, wspace=0.25, hspace=0.15)
plt.subplots_adjust(left=0.1, bottom=0.07,  right=0.98, top=0.98)
plt.tight_layout()

ax[0,0].set_title(r'$\pi^{+}$',fontsize=30,color = 'blue')
ax[0,1].set_title(r'$\pi^{-}$',fontsize=30,color = 'blue')
ax[0,2].set_title(r'$K^{+}$',fontsize=30,color = 'blue')
ax[0,3].set_title(r'$K^{-}$',fontsize=30,color = 'blue')

ax[2,0].set_title(r'$p$',fontsize=30,color = 'blue')
ax[2,1].set_title(r'$\bar{p}$',fontsize=30,color = 'blue')
#ax[2,2].set_title(r'$\Lambda$',fontsize=30,color = 'blue')
#ax[2,3].set_title(r'$\bar{\Lambda}$',fontsize=30,color = 'blue')

ax[4,0].set_title(r'$K^{*0}$',fontsize=30,color = 'blue')
ax[4,1].set_title(r'$\bar{K^{*0}}$',fontsize=30,color = 'blue')
ax[4,2].set_title(r'$\phi$',fontsize=30,color = 'blue')



# settting the position of plots
axis0 = ax[0,0].get_position()
ax[0,1].set_position([axis0.x0 + 0.31, axis0.y0 , axis0.width, axis0.height ])
ax[0,2].set_position([axis0.x0 + 0.62, axis0.y0 , axis0.width, axis0.height ])
ax[0,3].set_position([axis0.x0 + 0.92, axis0.y0 , axis0.width, axis0.height ])

ax[1,0].set_position([axis0.x0, axis0.y0 - 0.092, axis0.width, axis0.height * 0.4])
ax[2,0].set_position([axis0.x0, axis0.y0 - 0.320, axis0.width, axis0.height ])
ax[3,0].set_position([axis0.x0, axis0.y0 - 0.403, axis0.width, axis0.height * 0.4])
ax[4,0].set_position([axis0.x0, axis0.y0 - 0.633, axis0.width, axis0.height ])
ax[5,0].set_position([axis0.x0, axis0.y0 - 0.723, axis0.width, axis0.height * 0.4])

axis0 = ax[0,1].get_position()
ax[1,1].set_position([axis0.x0, axis0.y0 - 0.092, axis0.width, axis0.height * 0.4])
ax[2,1].set_position([axis0.x0, axis0.y0 - 0.320, axis0.width, axis0.height ])
ax[3,1].set_position([axis0.x0, axis0.y0 - 0.403, axis0.width, axis0.height * 0.4])
ax[4,1].set_position([axis0.x0, axis0.y0 - 0.633, axis0.width, axis0.height ])
ax[5,1].set_position([axis0.x0, axis0.y0 - 0.723, axis0.width, axis0.height * 0.4])

axis0 = ax[0,2].get_position()
ax[1,2].set_position([axis0.x0, axis0.y0 - 0.092, axis0.width, axis0.height * 0.4])
ax[2,2].set_position([axis0.x0, axis0.y0 - 0.320, axis0.width, axis0.height ])
ax[3,2].set_position([axis0.x0, axis0.y0 - 0.403, axis0.width, axis0.height * 0.4])
ax[4,2].set_position([axis0.x0, axis0.y0 - 0.633, axis0.width, axis0.height ])
ax[5,2].set_position([axis0.x0, axis0.y0 - 0.723, axis0.width, axis0.height * 0.4])


axis0 = ax[0,3].get_position()
ax[1,3].set_position([axis0.x0, axis0.y0 - 0.092, axis0.width, axis0.height * 0.4])
ax[2,3].set_position([axis0.x0, axis0.y0 - 0.320, axis0.width, axis0.height ])
ax[3,3].set_position([axis0.x0, axis0.y0 - 0.403, axis0.width, axis0.height * 0.4])
ax[4,3].set_position([axis0.x0, axis0.y0 - 0.633, axis0.width, axis0.height ])
ax[5,3].set_position([axis0.x0, axis0.y0 - 0.723, axis0.width, axis0.height * 0.4])


# sharing axis properties
ax[0,0].get_shared_x_axes().join(ax[0,0], ax[0,1],ax[0,2],ax[0,3])
ax[0,0].get_shared_y_axes().join(ax[0,0], ax[0,1],ax[0,2],ax[0,3])
ax[1,0].get_shared_x_axes().join(ax[1,0], ax[1,1],ax[1,2],ax[1,3])
ax[1,0].get_shared_y_axes().join(ax[1,0], ax[1,1],ax[1,2],ax[1,3])
ax[2,0].get_shared_x_axes().join(ax[2,0], ax[2,1],ax[2,2],ax[2,3])
ax[2,0].get_shared_y_axes().join(ax[2,0], ax[2,1],ax[2,2],ax[2,3])
ax[3,0].get_shared_x_axes().join(ax[3,0], ax[3,1],ax[3,2],ax[3,3])
ax[3,0].get_shared_y_axes().join(ax[3,0], ax[3,1],ax[3,2],ax[3,3])




for ii in range(0,6):
  for jj in range(0,4):
    ax[ii,jj].set_xlim(-0.99,0.99)

for ii in range(0,6,2):
  for jj in range(0,4):
    ax[ii,jj].set_ylim(-0.02,0.02)
    ax[ii,jj].set_yscale('linear')
    ax[ii,jj].set_ylabel(r'$v_1$', fontsize = 25)


for ii in range(1,6,2):
  for jj in range(0,4):
    ax[ii,jj].set_ylim(0.05,2.5)
    ax[ii,jj].set_ylabel('$ratio$', fontsize = 15)
    ax[ii,jj].set_xlabel('$y$ ', fontsize = 25)


ax[4,3].xaxis.set_visible(False)
ax[5,3].xaxis.set_visible(False)
ax[4,3].yaxis.set_visible(False)
ax[5,3].yaxis.set_visible(False)

ax[2,2].xaxis.set_visible(False)
ax[2,2].yaxis.set_visible(False)
ax[3,2].xaxis.set_visible(False)
ax[3,2].yaxis.set_visible(False)

ax[2,3].xaxis.set_visible(False)
ax[2,3].yaxis.set_visible(False)
ax[3,3].xaxis.set_visible(False)
ax[3,3].yaxis.set_visible(False)
#ax[0,1].yaxis.set_ticklabels([])


for ii in range(0,6):
  for jj in range(0,4):
    ax[ii,jj].minorticks_on()


#ax[1,0].xaxis.set_minor_locator(MultipleLocator(10))
#ax[1,0].xaxis.set_minor_formatter('{x:.0f}')

for ii in range(0,6):
  for jj in range(0,4):
    ax[ii,jj].tick_params(axis='both', which='major', labelsize=25, direction = 'in', left = True, right = True, bottom = True, width = 1.5 , length = 6.0 )
    ax[ii,jj].tick_params(axis='both', which='minor', labelsize=25, direction = 'in', left = True, right = True, bottom = True, width = 1.5, length = 2.0 )

#ax[1,0].set_yticks([1, 3])


A100, B100 = [],[]
A100.append(-5)
B100.append(0)
A100.append(5)
B100.append(0)


A200, B200 = [],[]
A200.append(-5)
B200.append(1)
A200.append(5)
B200.append(1)


for ii in range(1,6,2):
  for jj in range(0,4):
    ax[ii,jj].plot(A200, B200, ls = ':', linewidth = 0.8, color = 'black' )



# ===========================    PLOT    =========================== #


PARTS = [
'/v1_y-211_pT_0.15_3.dat',
'/v1_y--211_pT_0.15_3.dat',
'/v1_y-321_pT_0.15_3.dat',
'/v1_y--321_pT_0.15_3.dat',
'/v1_y-2212_pT_0.15_3.dat',
'/v1_y--2212_pT_0.15_3.dat',
'/v1_y-3122_pT_0.15_3.dat',
'/v1_y--3122_pT_0.15_3.dat',
'/v1_y-313_pT_0.15_3.dat',
'/v1_y--313_pT_0.15_3.dat',
'/v1_y-333_pT_0.15_3.dat',
]

WHERE_TO_PLOT_ROW = [0,0,0,0,2,2,2,2,4,4,4,4]
WHERE_TO_PLOT_COL = [0,1,2,3,0,1,2,3,0,1,2,3]

WHERE_RATIO_ROW = [1,1,1,1,3,3,3,3,5,5,5,5]
WHERE_RATIO_COL = [0,1,2,3,0,1,2,3,0,1,2,3]

A1, B1, ERR1,LBB1,UBB1 = [],[],[],[],[]
A2, B2, ERR2,LBB2,UBB2 = [],[],[],[],[]
P1,R1 = [],[]

for ix in range(0,int(len(PARTS))): 

  FILE1 = 'lower_mult_proxy_cut58.0upper_mult_proxy_cut187.9two_component_baryon_deposition_parameter_omega0.11matter_tilt_param1.1turn_on_baryon_diffusion1kappa_coefficient1.0epsilon_freeze0.11input_read_mode3include_weak_decay1/'
  FILE1 += PARTS[ix] 

  file1 = open(FILE1, 'r')
  Lines = file1.readlines()

  count = 0
  for line in Lines:
    count += 1
    if count > 1 :
      values = [float(s) for s in line.split()]
      A1.append(values[0])                       
      B1.append(values[1]) 
      ERR1.append(values[2])
      LBB1.append(values[1]-values[2]) 
      UBB1.append(values[1]+values[2]) 


  FILE2 = 'lower_mult_proxy_cut58.0upper_mult_proxy_cut187.9two_component_baryon_deposition_parameter_omega0.11matter_tilt_param1.1turn_on_baryon_diffusion1kappa_coefficient1.0epsilon_freeze0.11input_read_mode2include_weak_decay1/'
  FILE2 += PARTS[ix] 

  file1 = open(FILE2, 'r')
  Lines = file1.readlines()

  count = 0
  for line in Lines:
    count += 1
    if count > 1 :
      values = [float(s) for s in line.split()]
      A2.append(values[0])                       
      B2.append(values[1]) 
      ERR2.append(values[2])
      LBB2.append(values[1]-values[2]) 
      UBB2.append(values[1]+values[2]) 


  if ix == 3 :
    ax[WHERE_TO_PLOT_ROW[ix],WHERE_TO_PLOT_COL[ix]].plot(A1, B1, ls = '-', linewidth = 2.0, color = 'blue', label = '(iSS + Resonance Decay) $\epsilon_{f} = 0.11$ GeV/fm$^3$')
    ax[WHERE_TO_PLOT_ROW[ix],WHERE_TO_PLOT_COL[ix]].plot(A2, B2, ls = '-.', linewidth = 2.0, color = 'limegreen', label = '(iSS + UrQMD) $\epsilon_{f} = 0.11$ GeV/fm$^3$')
  else :
    ax[WHERE_TO_PLOT_ROW[ix],WHERE_TO_PLOT_COL[ix]].plot(A1, B1, ls = '-', linewidth = 2.0, color = 'blue')
    ax[WHERE_TO_PLOT_ROW[ix],WHERE_TO_PLOT_COL[ix]].plot(A2, B2, ls = '-.', linewidth = 2.0, color = 'limegreen')

  ax[WHERE_TO_PLOT_ROW[ix],WHERE_TO_PLOT_COL[ix]].fill_between(A1,LBB1, UBB1 ,facecolor='r',alpha=0.2, color = 'blue')
  ax[WHERE_TO_PLOT_ROW[ix],WHERE_TO_PLOT_COL[ix]].fill_between(A2,LBB2, UBB2 ,facecolor='r',alpha=0.2, color = 'limegreen')


  if ix !=6 and ix != 7 :
  # P stands for points and R stands for Ratio
    for i in range(count-2):
      if B2[i] != 0 and B1[i] != 0 :
        P1.append(A1[i])
        R1.append(B1[i]/B2[i])

    ax[WHERE_RATIO_ROW[ix]][WHERE_RATIO_COL[ix]].scatter(P1, R1, marker = 'o', s =10,  color = 'darkorange',facecolors='darkorange',linewidth = 2.5)

  A1.clear()
  B1.clear()
  ERR1.clear()
  LBB1.clear()
  UBB1.clear()
  A2.clear()
  B2.clear()
  ERR2.clear()
  LBB2.clear()
  UBB2.clear()
  P1.clear()
  R1.clear()




ax[0,3].legend(fontsize = 15, frameon = False)
#ax[2,1].legend(fontsize = 25, frameon = False)
#ax[0,2].legend(fontsize = 25, frameon = False)
ax[4,3].text(-0.7, 0.0 , r'Au+Au @27 GeV', fontsize=30, color = 'black')

plt.savefig('Plot_effect_of_hadronic_afterburner.pdf', format = 'pdf',bbox_inches='tight')

