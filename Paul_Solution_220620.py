"""
Credit Card Checker
===================
How do we know that the credit card number someone entered on our lounge is correct?
How do we know it is valid for the type of credit card they specified? Create a program
which allows the user to specify a credit card number and the card type (Visa,
Mastercard, American Express or Discover) and return a message if the number is valid
or an error message if the credit card number is invalid.
"""

# Card dictionary that holds all the credit card information.
# I can use a list [] or tuple () but a dictionary {} allows me to call by name.

# ================================================
# ==  Dictionaries
# ================================================
pass_check = {
    "type": False,
    "length": False,
    "isnumbers": False,
    "correctprefix": False
}  # used to monitor checks

cc_dict = {
    '1': {"name": "visa", "iin": [4], "length": [16]},
    '2': {"name": "mastercard", "iin": [[2221, 2720], [51, 55]], "length": [16]},
    '3': {"name": "amex", "iin": [34, 37], "length": [15]},
    '4': {"name": "discover", "iin": [[6011], [622126, 622925], [624000, 626999], [628200, 628899], [64], [65]],
          "length": [16, 19]},
}  # used to hold card data

# ================================================
# ==  Main
# ================================================

# user input credit card type
while pass_check['type'] is False:
    creditCardtype = input(
        'which type of card is it: \n1. Visa\n2. Mastercard\n3. Amex\n4. Discover\nPlease enter the correspondiing number: ')

    if creditCardtype not in ['1', '2', '3', '4']:  # make sure selected between 1-4 for credit card type
        print("\n**** PLEASE ENTER BETWEEN 1 AND 4 ****\n")
    else:
        pass_check['type'] = True
        cc_type = cc_dict[creditCardtype]

# user input credit card number
while pass_check['length'] is False or pass_check['correctprefix'] is False:
    creditCardNumber = input('please enter full credit card number: ')

    if len(cc_type['length']) > 1:  # Check if length of card number is a range.
        if len(creditCardNumber) >= cc_type['length'][0] and len(creditCardNumber) <= cc_type['length'][1]:
            pass_check['length'] = True
        else:
            # use a formatted string (aka: f-string pass variables into a string)
            print(
                f"\n**** Card length does not match card type, {cc_type['name']} has a card length range of {cc_type['length'][0]} to {cc_type['length'][1]}:  ****\n")
            break

    elif len(creditCardNumber) == cc_type['length'][0]:  # Select the first number of the list
        pass_check['length'] = True
    else:
        # use a formatted string (aka: f-string pass variables into a string)
        print(
            f"\n**** Card length does not match card type, {cc_type['name']} has a card length of {cc_type['length'][0]}:  ****\n")
        break

    # Work out the prefix
    if len(cc_type['iin']) == 1:
        if str(cc_type['iin'][0]) == str(creditCardNumber[:len(str(cc_type['iin'][0]))]):
            pass_check['correctprefix'] = True
        else:
            print(f"\n**** Card prefix does not match card number:  ****\n")
            break
    elif len(cc_type['iin']) > 1:
        for i in cc_type['iin']:
            if pass_check['correctprefix'] != True:
                if len(i) == 1:
                    if str(i[0]) == str(creditCardNumber[:len(str(i[0]))]):
                        pass_check['correctprefix'] = True
                    # else:
                    #     print(f"\n**** Card prefix does not match card number:  ****\n")
                    #     break
                elif len(i) > 1:
                    if int(creditCardNumber[:len(str(i[0]))]) >= int(i[0]) and int(
                            creditCardNumber[:len(str(i[0]))]) <= int(i[1]):
                        pass_check['correctprefix'] = True
                    # else:
                    #     print(f"\n**** Card prefix does not match card number:  ****\n")
                    #     break
        if pass_check['correctprefix'] == False:
            print(f"\n**** Card prefix does not match card number:  ****\n")

# apply luhn algorithm
algorithm = []
for i, d in enumerate(creditCardNumber[::-1]):
    d = int(d)
    if i == 0:
        pass
    elif (i % 2) == 0:
        algorithm.append(d)
    else:
        if d * 2 > 9:
            algorithm.append((d * 2) - 9)
        else:
            algorithm.append(d * 2)

checksum = (sum(algorithm[::-1]) * 9) % 10
if checksum == int(creditCardNumber[-1]):
    checksum_out = "Valid"
else:
    checksum_out = "Invalid"

print("\n\n *****************************\n",
      f"Card Number: {creditCardNumber} \n Card Type: {cc_type['name'].title()} \n Check Sum: {checksum} - {checksum_out} ",
      "\n *****************************\n\n")