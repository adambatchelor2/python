# Create a program which allows the user to specify a credit card number and the card type (Visa, Mastercard
# , American Express or Discover) and return a message if the number is valid or an error message if the credit card number is invalid.

# This program is all based around the idea of the Luhn algorithm (Check Wikipedia for “Luhn Algorithm”). 
# This algorithm can be used to validate credit card numbers. First make sure the number they entered is the
# correct number of digits and of the correct number prefix (Check out Wikipedia for “Bank card number” for more information).
# Once you determine the correct prefix and the right number of digits, you can then try applying the algorithm.

def isitLuhn (card_no):
	#reverse card no
	card_no = card_no[::-1]

	#empty list
	list1 = []

	#double every other value in reversed list
	for x in range(1,len(card_no),2):
		list1.append(int(card_no[x])*2)

	#drop to less than 10
	for x,i in enumerate(list1):
		if i > 9:
			list1[x] = (i - 9)

	#add back in rest of card no
	for x in range(0,len(card_no),2):
		list1.append(int(card_no[x]))		

	#sum all digits
	sum_list = sum(list1)

	#mod of 10 is 0 then valid
	if sum_list%10==0:
		return ("valid")
	else:
		return ("invalid")


print(isitLuhn("123456789101112"))
