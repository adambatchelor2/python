with open("aoc6.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n\n") #split data into groups - still have /n inside
count_uniq = 0
final_count = 0

# Part 1:
# for x in y: # loop through groups
#     uniq_list = []
#     z = x.split("\n") #split eaceh group into mini list
#
#     all = (''.join(map(str, z))) #combine list items together
#
#     for a in range(0,len(all)):
#         if all[a] not in uniq_list:
#             uniq_list.append(all[a])
#
#     count_uniq = len(uniq_list)
#     final_count += count_uniq
#     uniq_list = []
#
# print(final_count)

# Part 2:
for x in y: # loop through groups
    uniq_list = []
    z = x.split("\n") #split eaceh group into mini list
    mydict = {}
    count_uniq = 0
    group_size = len(z)

    for a in z:
        for b in range(0,len(a)):
            if a[b] in mydict:
                mydict[a[b]] += 1
            else:
                mydict[a[b]] = 1

    for key, value in mydict.items():
        if value == group_size:
            count_uniq += 1

    final_count += count_uniq

print(final_count)