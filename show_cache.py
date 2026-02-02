from sklearn.datasets import get_data_home
import os

dh = get_data_home()
print('DATA_HOME:', dh)

if os.path.exists(dh):
    for root, dirs, files in os.walk(dh):
        print(root)
        for f in files:
            print('  ', f)
else:
    print('Data home does not exist')
