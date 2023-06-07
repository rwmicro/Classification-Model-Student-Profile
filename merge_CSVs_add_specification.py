import pandas as pd

interest = pd.read_csv('data/student_interests.csv')
grades = pd.read_csv('data/student_grades.csv')

interest['student_id'] = interest['student_id'].astype(str)
grades['student_id'] = grades['student_id'].astype(str)

final = pd.merge(interest, grades[['student_id', 'junior_network_administrator',
                 'junior_web_programmer', 'junior_programmer']], on='student_id')

for i in range(final.shape[0]):
    junior_network_administrator = final.loc[i, 'junior_network_administrator']
    junior_web_programmer = final.loc[i, 'junior_web_programmer']
    junior_programmer = final.loc[i, 'junior_programmer']
    dic = {"Junior Network Administrator": junior_network_administrator,
           "Junior Web Programmer": junior_web_programmer,
           "Junior Programmer": junior_programmer}
    max_value = max(dic.values())
    for key, value in dic.items():
        if value == max_value:
            max_key = key
            break
    final.at[i, 'specification'] = key

final.to_csv('data/datas.csv', index=False)
print("The file 'dataset.csv' has been created in the folder data.")
