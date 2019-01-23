import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib

import molsim_utilities as mu

'''
print()
print('Using Path.glob to search for *.list files in test/:')
for p in sorted(Path('test/').glob('*.list')):
    print('  p:\t ', p)
    print('  p.parts: ', p.parts)
    print('  p.parts[0]: ', p.parts[0])
    print('  p.parts[1]: ', p.parts[1])
    print('  p.parts[1][2:5]: ', p.parts[1][2:5])
    print('  p.parts[1][:-5]: ', p.parts[1][:-5])
    print('  p.parts[1][-4:]: ', p.parts[1][-4:])

    
# Path.rglob recursively searches for files (i.e. it includes all sub-folders)
print()
print('Using Path.glob to _recursively_ search for *.list files in test/:')
for p in sorted(Path('test/').rglob('*.list')):
    print('  p:\t ', p, '    p.parts: ', p.parts)
    #print('  p.parts: ', p.parts)

print()

# only search for .list files in foldes which start with ph
print('Using Path.glob to _recursively_ search for *.list files in test/ph*:')
for p in sorted(Path('test/').glob('ph*/*.list')):
    print('  p:\t ', p, '    p.parts: ', p.parts, )#'  pH: ', int(p.parts[1][2]))

print()

'''

# Extracting charge data from .out files
alpha_1 = []
alpha_2 = []
alpha_error_1 = []
alpha_error_2 = []
ph = []
for p in sorted(Path('test/alumina_silica/AlSi100/backup/').glob('pH*/*.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    charge_1 = mu.getAvgPartCharge(p, 'alumina')
    charge_2 = mu.getAvgPartCharge(p, 'silica')

    alpha_1.append( charge_1[0] )
    alpha_2.append( charge_2[0] )

    alpha_error_1.append( charge_1[2] )
    alpha_error_2.append( charge_2[2] )
    ph.append( int(p.parts[-2][2]) )

print('\n pH: ', ph, '\n alpha_1: ', alpha_1, '\n alpha_error: ', alpha_error_1)
print('\n pH: ', ph, '\n alpha_2: ', alpha_2, '\n alpha_error: ', alpha_error_2)

alpha_al = []
alpha_si = []
ph = []
for p in sorted(Path('test/alumina_silica/AlSi240/backup/').glob('pH*/*.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    
    charge = mu.getAvgPartCharge(p, 'alumina') 
    alpha_al.append( charge[0] )
    charge = mu.getAvgPartCharge(p, 'silica')
    alpha_si.append( charge[0] )    
    ph.append( int(p.parts[-2][2]) )


alpha_al500 = []
alpha_si500 = []
ph = []
for p in sorted(Path('test/alumina_silica/AlSi500/backup/').glob('pH*/*.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    
    charge = mu.getAvgPartCharge(p, 'alumina')
    alpha_al500.append( charge[0] )
    charge = mu.getAvgPartCharge(p, 'silica')
    alpha_si500.append( charge[0])
    ph.append( int(p.parts[-2][2]) )


 #Plot charge data


fig1, ax1 = plt.subplots(1,1)

ax1.set_xlabel('pH')
ax1.set_ylabel('Fractional charge')

ax1.plot(ph, alpha_1, marker='o', markersize=10, label='alumina (Al100)')#linestyle='None')
ax1.plot(ph, alpha_2, marker='v', markersize=10, label='silica (Si100)')
ax1.plot(ph, alpha_al, color='tab:orange', marker='o', markersize=10, label='alumina (Al240)')#linestyle='None')
ax1.plot(ph, alpha_si, color='tab:orange', marker='v', markersize=10, label='silica (Si240)')
ax1.plot(ph, alpha_al500, linestyle='--', marker='o', markersize=10, label='alumina (Al500)')#linestyle='None')
ax1.plot(ph, alpha_si500, linestyle='--', marker='v', markersize=10, label='silica (Si500)')

ax1.legend()


#fig1.savefig('alumina_silicatitration.pdf')


#Extract distributions from .list files and plot them

fig2, ax2 = plt.subplots(1,1)

for p in sorted(Path('test/').glob('pH*/*.list')):
    d = mu.getDistribution(p, 'rdf ion-counterion')    
    labelstring = 'pH = {:d}'.format( int(p.parts[1][2]) )
    ax2.plot( d[:,0], d[:,1], label=labelstring )  # d[:,0] extracts the first column from d, d[:,1] the second

ax2.legend()   # Show legend/labels in ax2
    
'''
Show plots
'''
plt.show()

