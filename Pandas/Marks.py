import pandas as pd

col101 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_101 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-101', usecols=col101, nrows=62)
temp101 = []
sum101 = []
for i in range(62):
    j = float(cse_101.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = float(abs(cse_101.iloc[i:i + 1]['Internal'] - cse_101.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_101.iloc[i:i + 1]['External'] - cse_101.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp101.append(float((cse_101.iloc[i:i + 1]['Internal'] + cse_101.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp101.append(float((cse_101.iloc[i:i + 1]['External'] + cse_101.iloc[i:i + 1]['3rd Examiner']) / 2))
    else:
        temp101.append(float((cse_101.iloc[i:i + 1]['Internal'] + cse_101.iloc[i:i + 1]['External']) / 2))

    sum101.append(float(temp101[i]) + float(cse_101[i:i + 1]['Tutorial(40)']))
# print(sum101)
temp101 = []
for i in sum101:
    if i >= 80:
        temp101.append(4.00)
    elif (i >= 75 and i < 80):
        temp101.append(3.75)
    elif i >= 70 and i < 75:
        temp101.append(3.50)
    elif i >= 65 and i < 70:
        temp101.append(3.25)
    elif i >= 60 and i < 65:
        temp101.append(3.00)
    elif i >= 55 and i < 60:
        temp101.append(2.75)
    elif i >= 50 and i < 55:
        temp101.append(2.50)
    elif i >= 45 and i < 50:
        temp101.append(2.25)
    elif i >= 40 and i < 45:
        temp101.append(2.00)
    else:
        temp101.append(0.00)
# print(temp101)


col103 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_103 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-103', usecols=col103, nrows=62)
temp103 = []
sum103 = []
for i in range(62):
    j = float(cse_103.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = float(abs(cse_103.iloc[i:i + 1]['Internal'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_103.iloc[i:i + 1]['External'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp103.append(float((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp103.append(float((cse_103.iloc[i:i + 1]['External'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))
    else:
        temp103.append(float((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['External']) / 2))

    sum103.append(float(temp103[i]) + float(cse_103[i:i + 1]['Tutorial']))
# print(sum103)
temp103 = []
for i in sum103:
    if i >= 80:
        temp103.append(4.00)
    elif (i >= 75 and i < 80):
        temp103.append(3.75)
    elif i >= 70 and i < 75:
        temp103.append(3.50)
    elif i >= 65 and i < 70:
        temp103.append(3.25)
    elif i >= 60 and i < 65:
        temp103.append(3.00)
    elif i >= 55 and i < 60:
        temp103.append(2.75)
    elif i >= 50 and i < 55:
        temp103.append(2.50)
    elif i >= 45 and i < 50:
        temp103.append(2.25)
    elif i >= 40 and i < 45:
        temp103.append(2.00)
    else:
        temp103.append(0.00)
# print(temp103)


col105 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_105 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-105', usecols=col105, nrows=62)
temp105 = []
sum105 = []
for i in range(62):
    j = float(cse_105.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = float(abs(cse_105.iloc[i:i + 1]['Internal'] - cse_105.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_105.iloc[i:i + 1]['External'] - cse_105.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp105.append(float((cse_105.iloc[i:i + 1]['Internal'] + cse_105.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp105.append(float((cse_105.iloc[i:i + 1]['External'] + cse_105.iloc[i:i + 1]['3rd Examiner']) / 2))
    else:
        temp105.append(float((cse_105.iloc[i:i + 1]['Internal'] + cse_105.iloc[i:i + 1]['External']) / 2))

    sum105.append(float(temp105[i]) + float(cse_105[i:i + 1]['Tutorial']))
# print(sum105)
temp105 = []
for i in sum105:
    if i >= 80:
        temp105.append(4.00)
    elif (i >= 75 and i < 80):
        temp105.append(3.75)
    elif i >= 70 and i < 75:
        temp105.append(3.50)
    elif i >= 65 and i < 70:
        temp105.append(3.25)
    elif i >= 60 and i < 65:
        temp105.append(3.00)
    elif i >= 55 and i < 60:
        temp105.append(2.75)
    elif i >= 50 and i < 55:
        temp105.append(2.50)
    elif i >= 45 and i < 50:
        temp105.append(2.25)
    elif i >= 40 and i < 45:
        temp105.append(2.00)
    else:
        temp105.append(0.00)
# print(temp105)


col107 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_107 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-107', usecols=col107, nrows=62)
temp107 = []
sum107 = []
for i in range(62):
    j = float(cse_107.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = float(abs(cse_107.iloc[i:i + 1]['Internal'] - cse_107.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_107.iloc[i:i + 1]['External'] - cse_107.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp107.append(float((cse_107.iloc[i:i + 1]['Internal'] + cse_107.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp107.append(float((cse_107.iloc[i:i + 1]['External'] + cse_107.iloc[i:i + 1]['3rd Examiner']) / 2))
    else:
        temp107.append(float((cse_107.iloc[i:i + 1]['Internal'] + cse_107.iloc[i:i + 1]['External']) / 2))

    sum107.append(float(temp107[i]) + float(cse_107[i:i + 1]['Tutorial']))
# print(sum107)
temp107 = []
for i in sum107:
    if i >= 80:
        temp107.append(4.00)
    elif (i >= 75 and i < 80):
        temp107.append(3.75)
    elif i >= 70 and i < 75:
        temp107.append(3.50)
    elif i >= 65 and i < 70:
        temp107.append(3.25)
    elif i >= 60 and i < 65:
        temp107.append(3.00)
    elif i >= 55 and i < 60:
        temp107.append(2.75)
    elif i >= 50 and i < 55:
        temp107.append(2.50)
    elif i >= 45 and i < 50:
        temp107.append(2.25)
    elif i >= 40 and i < 45:
        temp107.append(2.00)
    else:
        temp107.append(0.00)
# print(temp107)


col109 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_109 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-109', usecols=col109, nrows=62)
temp109 = []
sum109 = []
for i in range(62):
    j = float(cse_109.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = float(abs(cse_109.iloc[i:i + 1]['Internal'] - cse_109.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_109.iloc[i:i + 1]['External'] - cse_109.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp109.append(float((cse_109.iloc[i:i + 1]['Internal'] + cse_109.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp109.append(float((cse_109.iloc[i:i + 1]['External'] + cse_109.iloc[i:i + 1]['3rd Examiner']) / 2))
    else:
        temp109.append(float((cse_109.iloc[i:i + 1]['Internal'] + cse_109.iloc[i:i + 1]['External']) / 2))

    sum109.append(float(temp109[i]) + float(cse_109[i:i + 1]['Tutorial']))
# print(sum109)
temp109 = []
for i in sum109:
    if i >= 80:
        temp109.append(4.00)
    elif (i >= 75 and i < 80):
        temp109.append(3.75)
    elif i >= 70 and i < 75:
        temp109.append(3.50)
    elif i >= 65 and i < 70:
        temp109.append(3.25)
    elif i >= 60 and i < 65:
        temp109.append(3.00)
    elif i >= 55 and i < 60:
        temp109.append(2.75)
    elif i >= 50 and i < 55:
        temp109.append(2.50)
    elif i >= 45 and i < 50:
        temp109.append(2.25)
    elif i >= 40 and i < 45:
        temp109.append(2.00)
    else:
        temp109.append(0.00)
# print(temp109)


col111 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_111 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-111', usecols=col111, nrows=64)
temp111 = []
sum111 = []
for i in range(64):
    j = float(cse_111.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = float(abs(cse_111.iloc[i:i + 1]['Internal'] - cse_111.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_111.iloc[i:i + 1]['External'] - cse_111.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp111.append(float((cse_111.iloc[i:i + 1]['Internal'] + cse_111.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp111.append(float((cse_111.iloc[i:i + 1]['External'] + cse_111.iloc[i:i + 1]['3rd Examiner']) / 2))
    else:
        temp111.append(float((cse_111.iloc[i:i + 1]['Internal'] + cse_111.iloc[i:i + 1]['External']) / 2))

    sum111.append(2 * (float(temp111[i]) + float(cse_111[i:i + 1]['Tutorial'])))
# print(sum111)
temp111 = []
for i in sum111:
    if i >= 80:
        temp111.append(4.00)
    elif (i >= 75 and i < 80):
        temp111.append(3.75)
    elif i >= 70 and i < 75:
        temp111.append(3.50)
    elif i >= 65 and i < 70:
        temp111.append(3.25)
    elif i >= 60 and i < 65:
        temp111.append(3.00)
    elif i >= 55 and i < 60:
        temp111.append(2.75)
    elif i >= 50 and i < 55:
        temp111.append(2.50)
    elif i >= 45 and i < 50:
        temp111.append(2.25)
    elif i >= 40 and i < 45:
        temp111.append(2.00)
    else:
        temp111.append(0.00)
# print(temp111)


col108 = [0, 1, 2, 3, 4]
cse_108 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-108', usecols=col108, nrows=64)
temp108 = []
sum108 = []
for i in range(64):
    sum108.append(float(cse_108.iloc[i:i + 1]['Class test'] + cse_108.iloc[i:i + 1]['Final']))
# print(sum108)
temp108 = []
for i in sum108:
    if i >= 80:
        temp108.append(4.00)
    elif (i >= 75 and i < 80):
        temp108.append(3.75)
    elif i >= 70 and i < 75:
        temp108.append(3.50)
    elif i >= 65 and i < 70:
        temp108.append(3.25)
    elif i >= 60 and i < 65:
        temp108.append(3.00)
    elif i >= 55 and i < 60:
        temp108.append(2.75)
    elif i >= 50 and i < 55:
        temp108.append(2.50)
    elif i >= 45 and i < 50:
        temp108.append(2.25)
    elif i >= 40 and i < 45:
        temp108.append(2.00)
    else:
        temp108.append(0.00)
# print(temp108)


col114 = [0, 1, 2, 3, 4]
cse_114 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-114', usecols=col114, nrows=64)
temp114 = []
sum114 = []
for i in range(64):
    sum114.append(2 * float(cse_114.iloc[i:i + 1]['Class test'] + cse_114.iloc[i:i + 1]['Final']))
# print(sum114)
temp114 = []
for i in sum114:
    if i >= 80:
        temp114.append(4.00)
    elif (i >= 75 and i < 80):
        temp114.append(3.75)
    elif i >= 70 and i < 75:
        temp114.append(3.50)
    elif i >= 65 and i < 70:
        temp114.append(3.25)
    elif i >= 60 and i < 65:
        temp114.append(3.00)
    elif i >= 55 and i < 60:
        temp114.append(2.75)
    elif i >= 50 and i < 55:
        temp114.append(2.50)
    elif i >= 45 and i < 50:
        temp114.append(2.25)
    elif i >= 40 and i < 45:
        temp114.append(2.00)
    else:
        temp114.append(0.00)
# print(temp114)


col100 = [0, 1, 2]
cse_100 = pd.read_excel(r"G:\2-2\Data Communication\Lab\Book2.xlsx", sheet_name='CSE-100', usecols=col100, nrows=64)
temp100 = []
sum100 = []
for i in range(64):
    sum100.append(float(2 * cse_100.iloc[i:i + 1]['CSE-100']))
# print(sum100)
temp100 = []
for i in sum100:
    if i >= 80:
        temp100.append(4.00)
    elif (i >= 75 and i < 80):
        temp100.append(3.75)
    elif i >= 70 and i < 75:
        temp100.append(3.50)
    elif i >= 65 and i < 70:
        temp100.append(3.25)
    elif i >= 60 and i < 65:
        temp100.append(3.00)
    elif i >= 55 and i < 60:
        temp100.append(2.75)
    elif i >= 50 and i < 55:
        temp100.append(2.50)
    elif i >= 45 and i < 50:
        temp100.append(2.25)
    elif i >= 40 and i < 45:
        temp100.append(2.00)
    else:
        temp100.append(0.00)
# print(temp100)

result = []
for i in range(62):
    result.append(float(((3 * temp101[i]) + (3 * temp103[i]) + (3 * temp105[i]) + (3 * temp107[i]) + (
            3 * temp109[i]) + (2 * temp111[i]) + temp108[i] + temp114[i] + temp100[i]) / 20))





print(result)
b = int(input("Enter the roll"))
if b == 150028:
    print(result[b - 150028])
elif b == 150060:
    print(result[b - 150060])
else:
    b=b+2
    print(result[b - 160001])

