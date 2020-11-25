
# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    import re

    # x = re.search("(?:http:\\)[abz]", strIn)
    x = re.search("(?:https://|http://|www\.)([a-zA-Z0-9\-_+%&#!]+)", url)

    return x.group(1)

print (domain_name("www.icann.org"))