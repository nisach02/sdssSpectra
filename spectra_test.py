#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:14:17 2021

@author: nischal
"""


"""
Initial file to start the project from. Contains one working example.
File takes the JPAS-ID and fluxes, 
along with SDSS inputs, and plots SDSS spectra against JPAS.

I will upload a new file later on trying to make it a bit more clean and use more function.

AIM: TAKE INPUT FROM FILE : ID, PLATE, MJD, FIBRE-ID, JPAS-ID, AND SO ON
THEN TO PLOT THE SPECTRA
THEN TO PLOT A JPAS PICTURE IN THE SIDE
THEN OVERPLOT PICTURE WITH INFO ABOUT REDSHIFT, X-RAY AND SO ON...

"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# import seaborn as sns
# sns.set_style('white')


from astroML.datasets import fetch_sdss_spectrum

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.

from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=False)



#setting figure size
plt.rcParams['figure.figsize'] = [8,6]
#setting x and y ticks to true
# plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = 1
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = 1

#setting border frame because we are using seaborn,
#and plotting in the canvas of Spyder.


plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.2

#setting high dpi for images
plt.rcParams['figure.dpi'] = 80
plt.rcParams['savefig.dpi'] = 100



jpas  = pd.read_csv('0_8aper.csv')
jpas2 = pd.read_csv('1_0aper.csv')
jpas3 = pd.read_csv('1_5aper.csv')
jpas4 = pd.read_csv('3_0aper.csv')
jpas5 = pd.read_csv('4_0aper.csv')
jpas6 = pd.read_csv('6_0aper.csv')


jpas_err  = pd.read_csv('0_8err.csv')
jpas2_err = pd.read_csv('1_0err.csv')
jpas3_err = pd.read_csv('1_5err.csv')
jpas4_err = pd.read_csv('3_0err.csv')
jpas5_err = pd.read_csv('4_0err.csv')
jpas6_err = pd.read_csv('6_0err.csv')
# temp_jpas = jpas[jpas['JPAS_ID'].isin(['2241_13222','2243_9363'])]

# temp_jpas = jpas[jpas['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas2 = jpas2[jpas2['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas3 = jpas3[jpas3['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas4 = jpas4[jpas4['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas5 = jpas5[jpas5['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas6 = jpas6[jpas6['JPAS_ID'].isin(['2241_13222'])]



# temp_jpas_err  = jpas_err[jpas_err['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas2_err = jpas2_err[jpas2_err['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas3_err = jpas3_err[jpas3_err['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas4_err = jpas4_err[jpas4_err['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas5_err = jpas5_err[jpas5_err['JPAS_ID'].isin(['2241_13222'])]
# temp_jpas6_err = jpas6_err[jpas6_err['JPAS_ID'].isin(['2241_13222'])]





# tempframe = pd.concat( [temp_jpas,temp_jpas2,temp_jpas3,temp_jpas4,temp_jpas5,temp_jpas6])
# tempframe = tempframe.set_index('JPAS_ID').T.div(100).iloc[::2, :]


# tempframe_err = pd.concat([temp_jpas_err,temp_jpas2_err,temp_jpas3_err,temp_jpas4_err,temp_jpas5_err,temp_jpas6_err])
# tempframe_err1 = tempframe_err.set_index('JPAS_ID').T.div(100)


# plotting = tempframe.plot(marker = 'o', legend=False)
# plt.legend(['0.8', '1', '1.5', '3', '4', '6'])
# # plt.yscale('log')
# plt.xlabel('\u03BB [$\AA$]')
# plt.ylabel('Flux [1e$^{-17}$erg/s/cm$^2$/$\AA$]')
# plt.title('2470_9821')
# plt.show()



# plotting = tempframe.plot(marker = 'x', legend=False)
# plt.legend(['0.8', '1', '1.5', '3', '4', '6'])
# plt.yscale('log')
# plt.xlabel('\u03BB [nm]')
# plt.ylabel('log(Flux) [1e$^{-17}$erg/s/cm$^2$/$\AA$]')
# plt.title('2241_13222')
# plt.show()





#------------------------------------------------------------
# Fetch single spectrum
plate = 1326
mjd = 52764
fiber = 300

spec = fetch_sdss_spectrum(plate, mjd, fiber)

#------------------------------------------------------------
# Plot the resulting spectrum

# plotting = tempframe.plot(marker = 'o', legend=False, ax = ax)

# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(spec.wavelength(), spec.spectrum, '-k',  lw=1, label = 'spectrum')
# tempframe.plot(marker = 'o', ax = ax)

# # ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# ax.legend(['0.8', '1', '1.5', '3', '4', '6'])
# ax.set_title('2241_13222')


# # ax.set_xlim(3000, 10000)
# # ax.set_ylim(25, 300)

# ax.set_xlabel(r'$\lambda {(\rm \AA)}$')
# ax.set_ylabel('Flux [1e$^{-17}$erg/s/cm$^2$/$\AA$]')
# ax.set_title('Plate = %(plate)i, MJD = %(mjd)i, Fiber = %(fiber)i' % locals())

# plt.show()





#making a list of the wavelength points for JPAS
new_list = [3780, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 10070]

#making a list of flux to plot against the points
#1
sdss_jpas = jpas[jpas['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas = sdss_jpas.set_index('JPAS_ID').T.div(100).iloc[::2, :]

sdss_jpas_err = jpas_err[jpas_err['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas_err = sdss_jpas_err.set_index('JPAS_ID').T.div(100)['2241_13222']


#2
sdss_jpas2 = jpas2[jpas2['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas2 = sdss_jpas2.set_index('JPAS_ID').T.div(100).iloc[::2, :]

sdss_jpas_err2 = jpas2_err[jpas2_err['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas_err2 = sdss_jpas_err2.set_index('JPAS_ID').T.div(100)['2241_13222']


#3
sdss_jpas3 = jpas3[jpas3['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas3 = sdss_jpas3.set_index('JPAS_ID').T.div(100).iloc[::2, :]

sdss_jpas_err3 = jpas3_err[jpas3_err['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas_err3 = sdss_jpas_err3.set_index('JPAS_ID').T.div(100)['2241_13222']


#4
sdss_jpas4 = jpas4[jpas4['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas4 = sdss_jpas4.set_index('JPAS_ID').T.div(100).iloc[::2, :]

sdss_jpas_err4 = jpas4_err[jpas4_err['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas_err4 = sdss_jpas_err4.set_index('JPAS_ID').T.div(100)['2241_13222']


#5
sdss_jpas5 = jpas5[jpas5['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas5 = sdss_jpas5.set_index('JPAS_ID').T.div(100).iloc[::2, :]

sdss_jpas_err5 = jpas5_err[jpas5_err['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas_err5 = sdss_jpas_err5.set_index('JPAS_ID').T.div(100)['2241_13222']


#6
sdss_jpas6 = jpas6[jpas6['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas6 = sdss_jpas6.set_index('JPAS_ID').T.div(100).iloc[::2, :]

sdss_jpas_err6 = jpas6_err[jpas6_err['JPAS_ID'].isin(['2241_13222'])]
sdss_jpas_err6 = sdss_jpas_err6.set_index('JPAS_ID').T.div(100)['2241_13222']





plt.rcParams['figure.figsize'] = [9,6]

plt.plot(spec.wavelength()[::10], spec.spectrum[::10], '-k',  lw=1, alpha = 1, label = 'SDSS')

plt.plot(spec.wavelength(), spec.spectrum, '-k',  lw=1, alpha = 0.2)

plt.errorbar(new_list,sdss_jpas['2241_13222'],  fmt = '-o', yerr = sdss_jpas_err,  c = 'tab:blue', label = '0.8')
plt.errorbar(new_list,sdss_jpas2['2241_13222'], fmt = '-o', yerr = sdss_jpas_err2, c = 'tab:orange', label = '1.0')
plt.errorbar(new_list,sdss_jpas3['2241_13222'], fmt = '-o', yerr = sdss_jpas_err3, c = 'tab:green', label = '1.5')
plt.errorbar(new_list,sdss_jpas4['2241_13222'], fmt = '-o', yerr = sdss_jpas_err4, c = 'tab:red', label = '3.0')
plt.errorbar(new_list,sdss_jpas5['2241_13222'], fmt = '-o', yerr = sdss_jpas_err5, c = 'tab:purple', label = '4.0')
plt.errorbar(new_list,sdss_jpas6['2241_13222'], fmt = '-o', yerr = sdss_jpas_err6, c = 'tab:brown', label = '6.0')

plt.legend()
# plt.xlim(3700, 9250)
plt.ylim(0,max(sdss_jpas6['2241_13222'] + 2))
plt.xlabel('\u03BB [$\AA$]')
plt.ylabel('Flux [1e$^{-17}$erg/s/cm$^2$/$\AA$]')
plt.title('JPAS-ID: 2241-13222')
plt.show()



'''
for default cycling colors names:
one of the Tableau Colors from the 'T10' categorical palette (the default color cycle):
    {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 
     'tab:gray', 'tab:olive', 'tab:cyan'} (case-insensitive)

'''



"""
p = temp_jpas.set_index('JPAS_ID')

p.iloc[i,j] le row,column ko value dincha


# temp_jpas.set_index('JPAS_ID').T.plot()
# temp_jpas2.set_index('JPAS_ID').T.plot()


# plt.yscale('log')
# plt.xlabel('\u03BB [$\AA$]')
# plt.ylabel('log(Flux) [1e$^{-19}$erg/s/cm$^2$/$\AA$]')
# plt.text(0.25,1200,'Aperture = 0.8')
# plt.show()




# temp_jpas2.set_index('JPAS_ID').T.plot()
# plt.yscale('log')
# plt.xlabel('\u03BB [$\AA$]')
# plt.ylabel('log(Flux) [1e$^{-19}$erg/s/cm$^2$/$\AA$]')
# plt.text(0.25,16000,'Aperture = 6.0')
# plt.show()



df1 = pd.DataFrame(
    {
         "A": [100, 200, 300, 400],
         "B": [90, 80, 70, 50],
          "C": [10, 20, 30, 40],
     })
df1 = pd.DataFrame(
    {
         "A": [100, 200, 300, 400],
         "A_E": [90, 80, 70, 50],
          "B": [10, 20, 30, 40],
          "B_E": [1, 2, 3, 4],
     })

tempframe = pd.concat([temp_jpas,temp_jpas2])
tempframe.set_index('JPAS_ID').T.plot()





#plot error bars
ax = df.plot(figsize=(12,8), yerr = errors, legend = False)
#reset color cycle so that the marker colors match
ax.set_prop_cycle(None)
#plot the markers
df.plot(figsize=(12,8), style=['^-', 'o--', 'x-.', 'D-'], markersize=14, ax = ax)

plt.show()










headers = ['0378', '0390', '0400', '0410', '0420', '0430', '0440', '0450', '0460', 
           '0470', '0480', '0490', '0500', '0510', '0520', '0530', '0540', '0550', 
           '0560', '0570', '0580', '0590', '0600', '0610', '0620', '0630', '0640', 
           '0650', '0660', '0670', '0680', '0690', '0700', '0710', '0720', '0730', 
           '0740', '0750', '0760', '0770', '0780', '0790', '0800', '0810', '0820' ]


"""
