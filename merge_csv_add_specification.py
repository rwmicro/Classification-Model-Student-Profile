import pandas as pd

interest = pd.read_csv('data/test.csv')
grades = pd.read_csv('data/student_grades.csv')
final = pd.merge(interest, grades, on='student_id')

for i in range(final.shape[0]):
    junior_network_administrator = final.loc[i,'junior_network_administrator']
    junior_web_programmer = final.loc[i,'junior_web_programmer']
    junior_programmer = final.loc[i,'junior_programmer']
    dic = {"Junior Network Administrator": junior_network_administrator,
           "Junior Web Programmer": junior_web_programmer,
           "Junior Programmer" : junior_programmer}
    max_value = max(dic.values())
    for key,value in dic.items():
        if value == max_value:
            max_key = key
            break
    final.at[i, 'specification'] = key

final.to_csv('data/final.csv', index=False)
print("The file 'final.csv' has been created in the folder data.")