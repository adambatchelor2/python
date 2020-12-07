
import re
# test_list= ['ecl', 'iyr', 'hgt', 'eyr', 'pid', 'byr', 'hcl']

with open("aoc4.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n\n")
suc_count = 0

# Part 1
# for x in y:
#     out = re.findall("([a-z]{3}):",x)
#
#     if len(list(set(out) & set(test_list))) == 7:
#         suc_count +=1
#
# print(suc_count)
# print(y)

# Part 2
for x in y:
    out = re.findall("([a-z]{3}):([A-Za-z0-9#]*)",x)
    # print(x)
    mydict = {}
    for a in out:
        mydict[a[0]] = a[1]
    # print(mydict)
    # print(suc_count)
    count = 0
    if "byr" in mydict and "iyr" in mydict and "eyr" in mydict and "hgt" in mydict and "hcl" in mydict and "ecl" in mydict and "pid" in mydict:
        if len(mydict["byr"]) == 4 and int(mydict["byr"])>=1920 and int(mydict["byr"])<=2002:
            count +=1

        if len(mydict["iyr"]) == 4 and int(mydict["iyr"])>=2010 and int(mydict["iyr"])<=2020:
            count +=1

        if len(mydict["eyr"]) == 4 and int(mydict["eyr"])>=2020 and int(mydict["eyr"])<=2030:
            count +=1

        hgt = mydict["hgt"]
        hgt_m = hgt[-2:]
        if hgt_m == "cm" or hgt_m == "in":
            hgt_d = int(hgt[:len(hgt)-2])
        else:
            hgt_d = 0

        if (hgt_m=="cm" and hgt_d >=150 and hgt_d <= 193) or (hgt_m=="in" and hgt_d >=59 and hgt_d <= 76):
            count +=1

        if re.match("(#[a-f0-9]{6})",mydict["hcl"]) and len(mydict["hcl"]) == 7:
            count +=1

        eye = ['amb','blu','brn','gry','grn','hzl','oth']
        if mydict["ecl"] in eye:
            count+=1

        if re.match("([0-9]{9})",mydict["pid"]) and len(mydict["pid"]) == 9:
            count += 1

        if count==7:
            suc_count += 1

print(suc_count)
