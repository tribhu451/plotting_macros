import matplotlib.pyplot as plt
import sys
import math
import numpy as np
#plt.style.use('seaborn-whitegrid')

#         PLOTS
fig = plt.figure(figsize=(6, 5))
ax = fig.gca()
plt.margins(0.2)
plt.subplots_adjust(bottom=0.07, top = 0.98, right = 0.98)

plt.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=20, direction = 'in', left = True, right = True, width = 1.5 , length = 6.0 )
plt.tick_params(axis='both', which='minor', labelsize=20, direction = 'in', left = True, right = True, width = 1.5 , length = 3.0 )


FILE=[
'lower_mult_proxy_cut235.3upper_mult_proxy_cut1000.0eps_freeze_min0.11eps_freeze_max0.11epsilon_freeze0.11turn_on_baryon_diffusion1kappa_coefficient1.0/',
'lower_mult_proxy_cut235.3upper_mult_proxy_cut1000.0eps_freeze_min0.15eps_freeze_max0.15epsilon_freeze0.15turn_on_baryon_diffusion1kappa_coefficient1.0/',
'lower_mult_proxy_cut235.3upper_mult_proxy_cut1000.0eps_freeze_min0.2eps_freeze_max0.2epsilon_freeze0.2turn_on_baryon_diffusion1kappa_coefficient1.0/'
]

PART = [
'dndy_y-2212_pT_0.01_3.dat',
'dndy_y--2212_pT_0.01_3.dat'
]



##############     MODEL   ##################

######### (1) 
file1 = open(FILE[0]+PART[0], 'r')
Lines = file1.readlines()

count = 0
A1, B1, ERR1 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A1.append(values[0])                       
		B1.append(values[1]) 
		ERR1.append(values[2]) 



file1 = open(FILE[0]+PART[1], 'r')
Lines = file1.readlines()

count = 0
A2, B2, ERR2 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A2.append(values[0])                       
		B2.append(values[1])
		ERR2.append(values[2])  


B1mB2, B1mB2ERR = [],[]
for i in range(count-1):
	B1mB2.append(B1[i] - B2[i])
	B1mB2ERR.append( math.sqrt(ERR1[i]*ERR1[i] + ERR2[i]* ERR2[i]) )



######### (2) 
file1 = open(FILE[1]+PART[0], 'r')
Lines = file1.readlines()

count = 0
A3, B3, ERR3 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A3.append(values[0])                       
		B3.append(values[1]) 
		ERR3.append(values[2]) 



file1 = open(FILE[1]+PART[1], 'r')
Lines = file1.readlines()

count = 0
A4, B4, ERR4 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A4.append(values[0])                       
		B4.append(values[1]) 
		ERR4.append(values[2]) 


B3mB4,B3mB4ERR = [],[]
for i in range(count-1):
	B3mB4.append(B3[i] - B4[i])
	B3mB4ERR.append( math.sqrt(ERR3[i]*ERR3[i] + ERR4[i]* ERR4[i]) )





######### (3) 
file1 = open(FILE[2]+PART[0], 'r')
Lines = file1.readlines()

count = 0
A5, B5, ERR5 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A5.append(values[0])                       
		B5.append(values[1]) 
		ERR5.append(values[2]) 



file1 = open(FILE[2]+PART[1], 'r')
Lines = file1.readlines()

count = 0
A6, B6, ERR6 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A6.append(values[0])                       
		B6.append(values[1])
		ERR6.append(values[2])  


B5mB6,B5mB6ERR = [],[]
for i in range(count-1):
	B5mB6.append(B5[i] - B6[i])
	B5mB6ERR.append( math.sqrt(ERR5[i]*ERR5[i] + ERR6[i]* ERR6[i]) )



'''
######### (4) 
file1 = open(FILE7, 'r')
Lines = file1.readlines()

count = 0
A7, B7, ERR7 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A7.append(values[0])                       
		B7.append(values[1]) 
		ERR7.append(values[2]) 



file1 = open(FILE8, 'r')
Lines = file1.readlines()

count = 0
A8, B8, ERR8 = [],[],[]
for line in Lines:
	count += 1
	if count > 1 :
		values = [float(s) for s in line.split()]
		A8.append(values[0])                       
		B8.append(values[1]) 
		ERR8.append(values[2]) 


B7mB8, B7mB8ERR = [],[]
for i in range(count-1):
	B7mB8.append(B7[i] - B8[i])
	B7mB8ERR.append( math.sqrt(ERR7[i]*ERR7[i] + ERR8[i]* ERR8[i]) )

'''




#plotting the data
#plt.errorbar(XDATA,YDATA,yerr = ERRDATA ,ms = 10,fmt="o",markeredgewidth = 2, markeredgecolor='red', markerfacecolor='red',color = 'red',elinewidth=1.4, alpha = 0.8, capsize = 2,label ='BRAHMS 00-10%')
#plt.errorbar(NEGXDATA,YDATA,yerr = ERRDATA ,ms = 10,fmt="o",markeredgewidth = 2, markeredgecolor='red', markerfacecolor='red',color = 'red',elinewidth=1.4, alpha = 0.8, capsize = 2)


#plt.errorbar(X1,Y1,yerr = DERR1 ,ms = 10,fmt="o",markeredgewidth = 2, markeredgecolor='black', markerfacecolor='black',color = 'black',elinewidth=1.4, alpha = 0.6, capsize = 2, label = 'NA49 DATA Pb+Pb 17.3 GeV')
#plt.errorbar(X2,Y2,yerr = DERR2 ,ms = 10,fmt="o",markeredgewidth = 2, markeredgecolor='limegreen', markerfacecolor='limegreen',color = 'limegreen',elinewidth=1.4, alpha = 0.8, capsize = 2)


plt.plot(A1, B1mB2, ls = '-', linewidth = 1.5, color = 'red', label = r'$\epsilon_{f}=0.11$ GeV/fm$^3$')
plt.plot(A3, B3mB4, ls = '--', linewidth = 1.5,   color = 'blue', label = r'$\epsilon_{f}=0.15$ GeV/fm$^3$')
plt.plot(A5, B5mB6, ls = '-.', linewidth = 1.5, color = 'limegreen', label = r'$\epsilon_{f}=0.20$ GeV/fm$^3$')
#plt.plot(A7, B7mB8, ls = '-', linewidth = 1.5, color = 'cyan', label = r'$\eta_{0} = 1.8, \sigma_{-} = 1.0, C_B = 0.0$')



#plt.errorbar(A1, B1, yerr = ERR1 ,ms = 2,fmt="o",markeredgewidth = 2, markeredgecolor='none', markerfacecolor='blue',color = 'blue',elinewidth=1.4, alpha = 0.6, capsize = 2)
#plt.plot(A1, B1, ls = '-', linewidth = 1.5, color = 'blue', label = r'$p$')
#plt.errorbar(A2, B2, yerr = ERR2 ,ms = 10,fmt="o",markeredgewidth = 2, markeredgecolor='none', markerfacecolor='limegreen',color = 'limegreen',elinewidth=1.4, alpha = 0.6, capsize = 2)
#plt.plot(A2, B2, ls = '-', linewidth = 1.5, color = 'limegreen', label = r'$\bar{p}$')

plt.xlabel(r'$y$', fontsize = 20)
plt.ylabel(r'$\frac{dN^{p-\bar{p}}}{dy}$', fontsize = 20)
plt.yscale('linear')
plt.legend(fontsize = 14)

plt.xlim(-6.,6.)
plt.ylim(0,42)

#plt.text(-2.0, 2 , r'Au+Au @$62.4$ GeV', fontsize=20, color = 'black')
#plt.text(0.00, 1 , r'10-40% DATA is not available', fontsize=14, color = 'black')


plt.savefig('plot_y_vs_net_proton.pdf', format = 'pdf',bbox_inches='tight')





