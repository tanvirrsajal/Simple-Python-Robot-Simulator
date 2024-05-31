import numpy as np
from scipy.stats import ttest_ind, chisquare

# Given data
data = {
    "Number of Boxes": [4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8],
    "Avg. Time Finding Box (Me)": [3.8392, 3.8403, 3.8404, 3.8405, 3.8406, 1.2532, 1.2529, 1.2526, 1.2528, 1.2528, 2.106, 2.1045, 2.1038, 2.1151, 2.1066, 1.5065, 1.5064, 1.5064, 1.5065, 1.5065, 1.5055, 1.5058, 1.5055, 1.5059, 1.5058],
    "Avg. Time Finding Box (Colleague)": [0.00108, 0.00075, 0.00058, 0.00068, 0.00073, 0.0008, 0.00079, 0.00076, 0.00075, 0.00082, 0.00075, 0.00074, 0.00075, 0.00079, 0.00071, 0.0008, 0.00079, 0.00076, 0.00078, 0.00079, 0.00075, 0.00075, 0.00074, 0.00078, 0.00077],
    "Avg. Time Delivering Box (Me)": [7.1246, 7.2118, 7.0159, 7.1704, 7.0078, 8.6088, 8.3675, 8.0929, 7.4248, 8.303, 7.1894, 7.583, 7.3568, 7.6185, 7.6565, 7.82, 7.5531, 8.5636, 7.841, 8.0721, 8.9275, 8.2052, 7.6574, 7.8098, 8.469],
    "Avg. Time Delivering Box (Colleague)": [10.22256, 10.0744, 10.04327, 10.10568, 10.16062, 9.68905, 9.71939, 9.88943, 9.71376, 9.96104, 5.67447, 5.67247, 5.5669, 5.75345, 5.76824, 6.45192, 6.62114, 6.26633, 6.26905, 6.26114, 6.86793, 6.87494, 7.00758, 6.89074, 6.92644],
    "Total Execution Time (Me)": [74.2912, 73.8848, 72.7981, 71.8546, 73.9217, 80.7349, 81.8155, 81.573, 80.3744, 82.717, 94.5756, 96.7856, 95.151, 97.4291, 97.1363, 112.4981, 110.2404, 112.2676, 113.0941, 114.8151, 138.4851, 136.8342, 131.0297, 132.0554, 138.5852],
    "Total Execution Time (Colleague)": [55.40991, 54.21028, 55.32878, 55.40147, 55.32169, 64.59154, 64.75527, 63.94536, 65.65486, 64.96388, 93.03451, 91.34882, 93.26598, 89.66574, 91.998, 83.02083, 83.7007, 85.87087, 86.15219, 83.87605, 92.86547, 92.79515, 91.20435, 92.33948, 92.99349]
}

# Convert data to numpy arrays
number_of_boxes = np.array(data["Number of Boxes"])
avg_time_finding_me = np.array(data["Avg. Time Finding Box (Me)"])
avg_time_finding_colleague = np.array(data["Avg. Time Finding Box (Colleague)"])
avg_time_delivering_me = np.array(data["Avg. Time Delivering Box (Me)"])
avg_time_delivering_colleague = np.array(data["Avg. Time Delivering Box (Colleague)"])
total_execution_time_me = np.array(data["Total Execution Time (Me)"])
total_execution_time_colleague = np.array(data["Total Execution Time (Colleague)"])

# Perform t-tests
t_statistic_find, p_value_find = ttest_ind(avg_time_finding_me, avg_time_finding_colleague)
t_statistic_deliver, p_value_deliver = ttest_ind(avg_time_delivering_me, avg_time_delivering_colleague)
t_statistic_total, p_value_total = ttest_ind(total_execution_time_me, total_execution_time_colleague)

# Perform chi-square test
chi_statistic_boxes, p_value_boxes = chisquare(number_of_boxes)


# Print results

print("T-test for average time finding box:")
print("   t-statistic =", t_statistic_find)
print("   p-value =", p_value_find)
if p_value_find < 0.05:
    if t_statistic_find > 0:
        print("   My average time finding box is significantly worse than my colleague's.")
    else:
        print("   My average time finding box is significantly better than my colleague's.")
else:
    print("   No significant difference found in average time finding box.")

print("\nT-test for average time delivering box:")
print("   t-statistic =", t_statistic_deliver)
print("   p-value =", p_value_deliver)
if p_value_deliver < 0.05:
    if t_statistic_deliver > 0:
        print("   My average time delivering box is significantly worse than my colleague's.")
    else:
        print("   My average time delivering box is significantly better than my colleague's.")
else:
    print("   No significant difference found in average time delivering box.")

print("\nT-test for total execution time:")
print("   t-statistic =", t_statistic_total)
print("   p-value =", p_value_total)
if p_value_total < 0.05:
    if t_statistic_total > 0:
        print("   My total execution time is significantly worse than my colleague's.")
    else:
        print("   My colleaugues total execution time is significantly better than my colleague's.")
else:
    print("   No significant difference found in totaal executing time.")