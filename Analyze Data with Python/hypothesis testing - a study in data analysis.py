import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency


vein_pack_lifespans = familiar.lifespans(package='vein')
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(format(vein_pack_test.pvalue, '0.10f'))

if vein_pack_test.pvalue < 0.05:
    print("The Vein Pack is proven to make you live longer!")
else:
    print(' The vein pack is probably good for you somehow')

artery_pack_lifespans = familiar.lifespans(package='artery')

package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

if package_comparison_results.pvalue < 0.05:
    print(' the artery package guarantees even stronger results')
else:
    print(' the artery package is also a great product')

iron_contingency_table = familiar.iron_counts_for_package()

print(iron_contingency_table)

_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

if iron_pvalue < 0.05:
    print(' the artery package is proven to make you healthier')
else:
    print("while we can't say the artery package will help you, i bet its nice.")
