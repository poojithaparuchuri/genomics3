"""
Problem Set-4
ROC curve
"""

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc



labels = [
    1, 0, 0, 1, 1, 0, 0, 1, 0, 0,
    1, 0, 0, 1, 1, 1, 0, 1, 0, 0,
    1, 1, 0, 0, 1, 1, 1, 1, 1, 0,
    1, 0, 0, 0, 0, 0, 1, 0, 1, 0
]


# Update scores to be the difference between the non-coding and coding scores
scores = [
    (-238.06901314970324) - (-326.3498168602558), (-365.618118100441) - (-500.4452354574444), (-369.14952103775806) - (-497.25800550619897),
    (-276.2919860508234) - (-368.338625561781), (-310.63618726332686) - (-418.70169369011643), (-279.9423005371768) - (-395.06936217231714),
    (-316.55583552586285) - (-442.2378403533328), (-317.2604456074268) - (-426.15502839037185), (-269.58123187539354) - (-369.272922134747),
    (-316.75881698508437) - (-421.4008007687992), (-245.5634265802078) - (-331.52475165885215), (-392.42578648015456) - (-531.7928224275017),
    (-349.1739443036555) - (-477.3339623494004), (-296.2304641193157) - (-404.63935583143075), (-251.37369808390156) - (-352.7586725547902),
    (-267.344482711302) - (-360.98094467382725), (-339.32595829239773) - (-465.94554433490384), (-235.55683553877336) - (-313.8864694766583),
    (-380.4086464501328) - (-513.1788583133598), (-291.87085660349413) - (-404.570647486156), (-259.4139476714081) - (-347.4172863305972),
    (-278.6852521127172) - (-371.0068304916044), (-374.76166292452) - (-521.6899176123242), (-291.71693452122184) - (-404.7576667304431),
    (-246.74125693677158) - (-339.6243332815332), (-292.0318875548155) - (-397.2471387866173), (-269.0705751460126) - (-375.4520896906712),
    (-233.0073903678478) - (-322.78343771592887), (-266.677309084119) - (-362.4900660544039), (-337.5554894286422) - (-460.7500241172094),
    (-225.11412288794958) - (-297.90647472075807), (-335.35600782454645) - (-452.60162694726745), (-289.67588905291746) - (-404.78646439995134),
    (-281.5517384496109) - (-384.15572263333553), (-303.68501517429445) - (-408.01916407179647), (-308.3174563214244) - (-426.5408031314057),
    (-263.6939993305636) - (-352.55903518352494), (-313.3416426488991) - (-437.3530880955014), (-264.86974155475303) - (-354.75032806565423),
    (-318.60156394207166) - (-433.07037023699985)
]

if len(scores) != len(labels):
    raise ValueError("Scores and labels must have the same length")

# Sort labels and scores based on scores (descending order)
sorted_labels_scores = sorted(zip(labels, scores), key=lambda x: x[1], reverse=True)
sorted_labels, sorted_scores = zip(*sorted_labels_scores)

# Calculate True Positive Rate and False Positive Rate
tp_rate = [0]  # Start with 0 to include the point (0, 0) in the ROC curve
fp_rate = [0]
total_positives = sum(labels)
total_negatives = len(labels) - total_positives

for i in range(len(sorted_labels)):
    if sorted_labels[i] == 1:
        tp_rate.append(tp_rate[-1] + 1 / total_positives)
        fp_rate.append(fp_rate[-1])
    else:
        tp_rate.append(tp_rate[-1])
        fp_rate.append(fp_rate[-1] + 1 / total_negatives)

reversed_scores = [-x for x in scores]

# Compute ROC curve and ROC area for reversed scores
fpr, tpr, thresholds = roc_curve(labels, reversed_scores)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Reversed Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

