import pandas as pd
import math
import collections, itertools


trainPath = "2-data-1.txt"

df = pd.read_csv(trainPath, sep=",",header=None,encoding='utf-8')
df = df.dropna()
input_attr = int(input("Enter the attribute: "))
df1 = df.iloc[:,input_attr-1]
Class = df.iloc[:,-1]
df2 = Class
result = pd.concat([df1, df2], axis=1)
res_list = result.values.tolist()
sub_dict = collections.Counter(tuple(item) for item in res_list)
class_list = df2.values.tolist()
class_dict = collections.Counter(class_list)
# print("class_dict",class_dict)
total = sum(class_dict.values())
class_entropy = []
for k,v in class_dict.items():
    entropy = -(v/total)*math.log(v/total, 2)
    class_entropy.append(entropy)
final_class_entropy = sum(class_entropy)

entropy_list = []
def entropyCalculator(data, targetAttr):
    resultant = []
    for i in res_list:
        counter = res_list.count(i)
        if i not in resultant:
            resultant.append(i)
            resultant.append(counter)

    final_list = []
    for i in range(0,len(resultant)-1,2):
        final_list.append(resultant[i]+[resultant[i+1]])
    final_dict = {}
    total = 0
    # print("final_list",final_list)
    for i in final_list:
        if i[0] not in final_dict.keys():
            new_dict = {}
            new_dict[i[1]] = i[2]
            total+= i[2]
            final_dict[i[0]] = new_dict
        else:
            if i[1] not in new_dict.keys():
                dummy_dict={}
                dummy_dict[i[1]] = i[2]
                total+= i[2]
                final_dict[i[0]].update(dummy_dict)
            else:
                new_dict1 = {}
                new_dict1[i[1]] = i[2]
                total+= i[2]
                final_dict[i[0]].update(new_dict1)

    # print("final_dict",final_dict)
    sub_entropy_values = []
    for value in final_dict.values():
        temp_list = []
        for i in value.values():
            temp_list.append(i)
        sub_entropy_values.append(temp_list)
    # print("sub_entropy_values",sub_entropy_values)
    for i in sub_entropy_values:
        sub_entropy = []
        sub_total = sum(i)
        for x in i:
            sub_entropy_value = -(x/sub_total)*math.log(x/sub_total, 2)
            sub_entropy.append(sub_entropy_value)
        final_sub_entropy = sum(sub_entropy) * (sub_total/total)
        entropy_list.append(final_sub_entropy)
    return entropy_list


entropyCalculator(df2, df1)
final_entropy = sum(entropy_list)
information_gain = round((final_class_entropy - final_entropy),3)
result_str = "(63\n\n(IG "+str(information_gain)+")\n\n)"
print(result_str)

with open('63_2.txt', 'w') as f:
    f.write(result_str)
