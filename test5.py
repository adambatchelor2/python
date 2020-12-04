
import re

listIn = [('ecl', 'grn'), ('cid', '315'), ('iyr', '2012'), ('hgt', '192cm'), ('eyr', '2023'), ('pid', '873355140'), ('byr', '1925'), ('hcl', '#ceec03')]
mydict = {}

for x in listIn:
    # print (x[0])
    mydict[x[0]] = x[1]

count = 0

if len(mydict["byr"]) == 4 and int(mydict["byr"])>=1920 and int(mydict["byr"])<=2002:
    count +=1

if len(mydict["iyr"]) == 4 and int(mydict["iyr"])>=2010 and int(mydict["iyr"])<=2020:
    count +=1

if len(mydict["eyr"]) == 4 and int(mydict["eyr"])>=2020 and int(mydict["eyr"])<=2030:
    count +=1

hgt = mydict["hgt"]
hgt_m = hgt[-2:]
hgt_d = int(hgt[:len(hgt)-2])

if (hgt_m=="cm" and hgt_d >=150 and hgt_d <= 193) or (hgt_m=="in" and hgt_d >=59 and hgt_d <= 76):
    count +=1

if re.match("(#[a-f0-9]{6})",mydict["hcl"]) and len(mydict["hcl"]) == 7:
    count +=1

eye = ['amb','blu','brn','gry','grn','hzl','oth']
if mydict["ecl"] in eye:
    count+=1

if re.match("([0-9]{9})",mydict["pid"]) and len(mydict["pid"]) == 9:
    count += 1

print(count)
