#Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
#format_date("11/12/2019") ➞ "20191211"
#format_date("12/31/2019") ➞ "20193112"
#Return value should be a string.

def conv_date(date_str):

	year = date_str[6:10]
	month = date_str[0:2]
	day = date_str[3:5]
	
	return str(year)+str(day)+str(month)

print (conv_date("01/20/2019"))