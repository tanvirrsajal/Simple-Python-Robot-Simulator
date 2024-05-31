import numpy as np

# Data
data = {
    "8": {
        "finding": [0.000143051147461, 0.000211000442505, 0.000111103057861, 3.00811481476, 3.00733613968, 3.0058619976, 3.50615596771, 0.000354051589966, 0.000148057937622, 0.000277996063232, 3.00579309464, 3.00743699074, 3.01440000534, 3.51287317276, 0.000349044799805, 0.000118017196655, 9.51290130615e-05, 3.00583195686, 3.00691008568, 3.0126721859, 3.50801086426, 0.000982999801636, 0.000124931335449, 0.000275135040283, 3.00620293617, 3.00507521629, 3.00600099564, 3.51484489441, 0.000107049942017, 0.000116109848022, 0.000334024429321, 3.51068615913, 3.00853800774, 3.00676703453, 4.51097106934],
        "delivering": [6.7663500309, 10.1399719715, 7.02123498917, 9.34014582634, 11.5249660015, 10.1427669525, 6.66945385933, 7.22456908226, 9.88420391083, 6.92233395576, 8.79021310806, 9.36176395416, 9.76794886589, 7.48484897614, 6.36734700203, 9.0801410675, 6.42336297035, 7.33145809174, 9.08625984192, 10.3011071682, 6.83253502846, 6.97166705132, 9.43177199364, 6.9194521904, 8.1265001297, 8.8900308609, 10.2986140251, 6.42319297791, 6.77261090279, 9.88769102097, 6.92551898956, 8.12940096855, 9.34741282463, 13.0935180187, 7.65422296524],
        "execution": [138.485058069, 136.834216118, 131.029659986, 132.055429935, 138.585179806]
    },
    "6": {
        "finding": [0.000184059143066, 0.000110149383545, 0.000128030776978, 3.51121115685, 4.51180386543, 0.000396966934204, 0.000917911529541, 0.000227928161621, 3.50836396217, 4.51149201393, 0.000102996826172, 0.0003821849823, 0.000123023986816, 3.5077021122, 4.50758099556, 0.000122785568237, 0.000237941741943, 0.000452995300293, 4.01024603844, 5.01452279091, 0.000121116638184, 0.000638961791992, 0.000119924545288, 3.50654792786, 4.50977492332],
        "delivering": [7.42288708687, 7.92540311813, 7.97885084152, 7.22536206245, 7.39225292206, 7.88234114647, 9.29963207245, 7.73918199539, 6.4272608757, 6.56952810287, 8.27785396576, 7.97733902931, 7.0192501545, 7.47588014603, 7.02964711189, 8.27664995193, 8.57952404022, 8.17732405663, 6.77601885796, 6.4329020977, 8.08333396912, 8.22897005081, 7.92532110214, 6.819617033, 7.22405195236],
        "execution": [94.5756309032, 96.785556078, 95.1509709358, 97.4290950298, 97.1363461018]
    },
    "7": {
        "finding": [0.000102996826172, 0.000569105148315, 0.000469923019409, 3.00941181183, 3.00849890709, 4.51134181023, 0.000113010406494, 0.000313997268677, 0.00011682510376, 3.00606608391, 3.00658011436, 4.50982999802, 0.000140190124512, 0.000205039978027, 0.000871896743774, 0.502366065979, 3.00717687607, 4.00778198242, 0.000391006469727, 0.00025200843811, 0.00032901763916, 3.00412416458, 3.00682091713, 4.51573705673, 0.000742197036743, 0.000117063522339, 0.000133037567139, 3.00656199455, 3.00755381584, 4.51385998726],
        "delivering": [6.97023701668, 7.73112893105, 9.0327899456, 9.38229680061, 8.03690814972, 5.77754092216, 6.76943588257, 7.92625999451, 8.83504986763, 9.38917803764, 7.8363969326, 5.97380900383, 7.17464590073, 6.1160030365, 9.73628091812, 8.58290815353, 9.18731093407, 7.58511710167, 6.21910309792, 7.57259702682, 8.73049712181, 8.73614287376, 9.76779007912, 6.02472686768, 7.83411002159, 7.57327198982, 9.12654805183, 8.93222689629, 8.28418707848, 6.68830013275],
        "execution": [112.49811697, 110.240386009, 112.267564058, 113.094116926, 114.815063]
    },
    "5": {
        "finding": [2.50669384003, 0.000100135803223, 9.48905944824e-05, 1.00580096245, 2.50487613678, 0.000488996505737, 0.000372171401978, 1.00316905975, 2.50614404678, 0.000329971313477, 0.000288963317871, 1.00192284584, 0.00142192840576, 0.000313997268677, 0.000213861465454, 3.50815010071, 2.50592303276, 0.000104188919067, 0.000241041183472, 1.00238800049],
        "delivering": [9.27449178696, 6.92397618294, 6.9209959507, 9.23391604424, 9.58354902267, 6.47131085396, 7.1258430481, 10.2875192165, 9.48486995697, 6.32043719292, 6.92910504341, 9.63516020775, 6.61537194252, 7.27119708061, 10.027078866, 9.09888505936, 6.92963194847, 6.32929301262, 10.4775080681, 7.77859210968],
        "execution": [82.9512419701, 80.9948270321, 83.1349840164, 85.4531068802, 83.2651059628]
    },
    "4": {
        "finding": [2.00554704666, 2.00299811363, 2.00700211525, 2.00517892838, 2.00536417961, 2.00328397751, 2.0046620369, 2.00826001167, 2.00134205818, 2.00412988663, 2.00204801559, 2.00164008141, 2.0052549839, 2.00843405724, 2.00663781166, 2.00165104866, 2.00208806992, 2.00787687302, 2.0016040802, 2.00135707855],
        "delivering": [10.0325829983, 8.23031020164, 10.045014143, 8.12218809128, 8.2692501545, 10.0089828968, 10.1051299572, 8.23800206184, 8.76942896843, 8.12303805351, 9.58019709587, 7.57405400276, 8.07663297653, 10.0155928135, 10.0441968441, 8.25396299362, 8.78203892708, 8.47466897964, 9.27500605583, 7.6740128994],
        "execution": [66.3689219952, 67.187486887, 68.1970849037, 66.2403790951, 66.7814190388]
    }
}

# Extracting all values
finding_times = []
delivering_times = []
execution_times = []

for case in data.values():
    finding_times.extend(case["finding"])
    delivering_times.extend(case["delivering"])
    execution_times.extend(case["execution"])

# Calculating mean and standard deviation
mean_finding = np.mean(finding_times)
std_finding = np.std(finding_times)

mean_delivering = np.mean(delivering_times)
std_delivering = np.std(delivering_times)

mean_execution = np.mean(execution_times)
std_execution = np.std(execution_times)

# Printing results
print(f"Finding time - Mean: {mean_finding:.6f}, Standard Deviation: {std_finding:.6f}")
print(f"Delivering time - Mean: {mean_delivering:.6f}, Standard Deviation: {std_delivering:.6f}")
print(f"Execution time - Mean: {mean_execution:.6f}, Standard Deviation: {std_execution:.6f}")
