from fragment_copies import FragmentCopies
from statistics import mean
import matplotlib.pyplot as plt


for i in range(1000): # Run the entire process with 1000 simulations
    fragment = FragmentCopies()
    fragment.cfDNA_convert()
    fragment.ligation_process()
    fragment.pcr()
    #fragment.target_enrichment() # target enrichment takes about an hour to run
    fragment.calculate()

print(mean(fragment.fragment_amount_check)) # prints average of all total fragment amounts
print(mean(fragment.unique_count_check)) # prints average fo all total unique fragment amounts
print(mean(fragment.ge_recovery_rate_check)) # prints average of all GE recovery rates

fig, ax = plt.subplots(2,2) # created subplots with 2 rows and 2 columns just for spacing

# plot histogram of the frequency of total fragment count after 1000 simulations
ax[0,0].hist(fragment.fragment_amount_check, color = 'lightskyblue', edgecolor = 'k')
ax[0,0].set_title('Frequency of Fragment Count after 1000 Simulations')
ax[0,0].set(xlabel = 'Fragment Count', ylabel = 'Frequency')
ax[0,0].axvline(mean(fragment.fragment_amount_check), color = 'k', linestyle = 'dashed', linewidth = 1 ) # displays dashed vertical line at the mean

# plot histogram of the frequency of total unique fragment count after 1000 simulations
ax[0,1].hist(fragment.unique_count_check, color = 'coral', edgecolor = 'k')
ax[0,1].set_title('Frequency of Unique Fragment Count after 1000 Simulations')
ax[0,1].set(xlabel = 'Fragment Count', ylabel = 'Frequency')
ax[0,1].axvline(mean(fragment.unique_count_check), color = 'k', linestyle = 'dashed', linewidth = 1 ) # displays dashed vertical line at the mean

# plot histogram of the frequency of GE recovery rate after 1000 simulations
ax[1,0].hist(fragment.ge_recovery_rate_check, color = 'mediumpurple', edgecolor = 'k')
ax[1,0].set_title('GE Recovery Rate after 100 Simulations')
ax[1,0].set(xlabel = 'Percentage', ylabel = 'Frequency')
ax[1,0].axvline(mean(fragment.ge_recovery_rate_check), color = 'k', linestyle = 'dashed', linewidth = 1 ) # displays dashed vertical line at the mean

plt.show()

