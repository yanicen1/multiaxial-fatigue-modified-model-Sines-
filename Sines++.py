import pandas as pd

# Store values of mechanical properties of used material in the file 'mechanical_properties.csv'.
MP = pd.read_csv('mechanical_properties.csv')

# Ultimate tensile strength (MPa):
s_u = MP['sigma_u_MPa'][0]
# Shear Strength (MPa):
t_u = MP['tau_u_MPa'][0]
# Shear fatigue strength coefficient (MPa):
t_f = MP["tau'f_MPa"][0]
# Shear fatigue strength exponent:
b0 = MP["b0"][0]
# Fatigue strength coefficient (MPa):
s_f = MP["sigma'f_MPa"][0]
# Fatigue strength exponent:
b = MP["b"][0]

# Store parameters of fatigue paths in the file 'fatigue_tests.csv'.
FT = pd.read_csv('fatigue_tests.csv')

# SR_I2a is the square root of the amplitude of the second invariant of the stress deviator tensor.
SR_I2a = 1/(6**0.5)*(2*FT['sa_MPa']**2+6*FT['ta_MPa']**2)**0.5
# SR_I2m is the square root of the mean value of the second invariant of the stress deviator tensor.
SR_I2m = 1/(6**0.5)*(2*FT['sm_MPa']**2+6*FT['tm_MPa']**2)**0.5
# I1m is the mean value of the first invariant of the stress tensor.
I1m = FT['sm_MPa']
# I1a is the amplitude of the first invariant of the stress tensor.
I1a = FT['sa_MPa']
# N0 is the initial fatigue life (cycles).
N0 = ((1/t_f)**(1/b0)*SR_I2a**(1/b0))/2

# Si is the initial model data (Sinse++). It has to approach 1.
Si = ((SR_I2a/(t_f*(2*N0)**b0))**2 + (SR_I2m/t_u)**2)**0.5 + (1/s_u - 1/((3)**0.5*t_u))*I1m + \
     (1/(s_f*(2*N0)**b) - 1/((3)**0.5*(t_f*(2*N0)**b0)))*I1a

for i in range(len(FT)):
    while Si[i] > 1.00001:
        N0[i] = N0[i] / Si[i]
        Si[i] = ((SR_I2a[i]/(t_f*(2*N0[i])**b0))**2 + (SR_I2m[i]/t_u)**2)**0.5 + (1/s_u - 1/((3)**0.5*t_u))*I1m[i] + \
             (1/(s_f*(2*N0[i])**b) - 1/((3)**0.5*(t_f*(2*N0[i])**b0)))*I1a[i]

# Neq_pr is the predicted equivalent fatigue life.
Neq_pr = N0

Neq_s_pr = [0 for n in range(len(FT))]
Neq_t_pr = [0 for n in range(len(FT))]
for j in range(len(FT)):
    if FT['nu_t_Hz'][j] != FT['nu_s_Hz'][j] and FT['nu_t_Hz'][j] != 0 and FT['nu_s_Hz'][j] != 0:
        Neq_t_pr[j] = Neq_pr[j] / ((FT['nu_s_Hz'][j] / FT['nu_t_Hz'][j]) ** 0.5)
        Neq_s_pr[j] = FT['nu_s_Hz'][j] / FT['nu_t_Hz'][j] * Neq_t_pr[j]
    else:
        Neq_t_pr[j] = N0[j]
        Neq_s_pr[j] = N0[j]

# Ns_pr and Nt_pr c.
Nt_pr = pd.DataFrame({'col':Neq_t_pr})['col']
Ns_pr = pd.DataFrame({'col':Neq_s_pr})['col']

Npr = pd.DataFrame({"Neq_pr_cycles": Neq_pr, "Nt_pr_cycles": Nt_pr, "Ns_pr_cycles": Ns_pr})
FT = pd.concat([FT, Npr], axis=1)

# Number of values of predicted fatigue life that are out of 2- and 3-factor error.
F_E = [0 for n in range(len(FT))]
F_E_1 = [0 for n in range(len(FT))]
F_E_2 = [0 for n in range(len(FT))]
for j in range(len(FT)):
    if FT['Ns_pr_cycles'][j] < FT['Ns_cycles'][j]/2 and FT['Ns_pr_cycles'][j] > FT['Ns_cycles'][j]/3 or \
            FT['Ns_pr_cycles'][j] > 2*FT['Ns_cycles'][j] and FT['Ns_pr_cycles'][j] < 3*FT['Ns_cycles'][j]:
        F_E[j] = 'out of the 2-factor error'
        F_E_1[j] = 1
        F_E_2[j] = 0
    elif FT['Ns_pr_cycles'][j] < FT['Ns_cycles'][j]/3 or FT['Ns_pr_cycles'][j] > 3*FT['Ns_cycles'][j]:
        F_E[j] = 'out of the 3-factor error'
        F_E_1[j] = 1
        F_E_2[j] = 1
    else:
        F_E[j] = ''

print("Percentage of values of predicted fatigue life that are out of the ±2-factor error range:",
      (sum(F_E_1)/(len(FT))*100).__round__(1), '%')
print('Number of values of predicted fatigue life that are out of the ±2-factor error range:',
      sum(F_E_1), 'out of', len(FT))
print("Percentage of values of predicted fatigue life that are out of the ±3-factor error range:",
      (sum(F_E_2)/(len(FT))*100).__round__(1), '%')
print('Number of values of predicted fatigue life that are out of the ±3-factor error range:',
      sum(F_E_2), 'out of', len(FT))

F_E = pd.DataFrame({"Data_label": F_E})
FT = pd.concat([FT, F_E], axis=1)

import numpy as np
# AE is the mean value of the absolute error. You can use it to compare different models.
AE = (sum((np.log10(FT['Ns_pr_cycles']/FT['Ns_cycles']))**2)/(len(FT)-2))**0.5

# The saving the output to the 'result.csv' file.
FT.to_csv('result.csv')
print('Standard error:', AE.__round__(3), '/ a factor of ±', (10**(1+AE)/10).__round__(2))

# Data visualization
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=1.3)
sns.set_style("ticks")
f, ax = plt.subplots(figsize=(6, 6))
ax.set(xscale="log", yscale="log")
plt.plot([1, 100000000], [1, 100000000], 'k-', lw=1)
plt.plot([2, 200000000], [1, 100000000], 'k--', [3, 300000000], [1, 100000000], 'k-.', lw=1)
plt.plot([0.5, 50000000], [1, 100000000], 'k--', label='Factor of ±2', lw=1)
plt.plot([1/3, 100000000/3], [1, 100000000], 'k-.', label='Factor of ±3', lw=1)
sns.scatterplot(x=FT['Ns_cycles'], y=FT['Ns_pr_cycles'], hue=np.array(FT['Loading_path']), s=70)
plt.ylim(0.8*min(min(FT['Ns_pr_cycles']), min(FT['Ns_cycles'])), 1.25*max(max(FT['Ns_pr_cycles']), max(FT['Ns_cycles'])))
plt.xlim(0.8*min(min(FT['Ns_pr_cycles']), min(FT['Ns_cycles'])), 1.25*max(max(FT['Ns_pr_cycles']), max(FT['Ns_cycles'])))
plt.xlabel("Experimental fatigue life, $N_{ex}$ (cycles)")
plt.ylabel("Predicted fatigue life $N_{pr}$, (cycles)")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.show()
