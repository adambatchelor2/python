# Your open-plan office building has a scrolling message screen on the far wall. One day, you notice
#  that the messages are starting to glitch. Some of the lower case letters are being replaced by their
#   position in the alphabet ("a" = 1, "b" = 2, ..., "z" = 26). Given the glitched text, return the corrected message.

# message_glitch("T21e19d1y's m1r11e20i14g m5e20i14g w9l12 14o23 2e i14 20h5 3o14f5r5n3e r15o13.")
# ➞ "Tuesday's marketing meeting will now be in the conference room."

# Each group of numbers will always refer to one letter only (e.g. 14 = "n", not "ad").

decode = "T21e19d1y's m1r11e20i14g m5e20i14g w9l12 14o23"


al_lst = 'abcdefghijklmnopqrstuvwyxyz'
al_dct = {i:al_lst[i] for i in range(0,len(al_lst))}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for i in range(0,len(decode)-1):
	if is_number(decode[i]) and is_number(decode[i+1]):
		char = int(decode[i]+decode[i+1])
		print(al_dct[char])