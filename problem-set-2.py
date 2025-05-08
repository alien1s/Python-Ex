###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1 # uncomment this to test with different input

marker1 = "AFK"
replacement1 = "away from keyboard"
line1 = "I will now go to sleep and be AFK until lunch time tomorrow."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

replaced1_position_start = line1.find(marker1)
line1_part1 = line1[:replaced1_position_start]
marker1_start = line1.find(marker1)
space = ' '
marker1_length = len(marker1)
marker1_end_by_space = line1.find(space ,marker1_start)-1
marker1_end_by_len = marker1_start + marker1_length-1
line1_part2 = line1[marker1_end_by_len+1:]
replaced1 = line1_part1 + replacement1 + line1_part2
print(replaced1)


# Example 2 # uncomment this to test with different input
marker2 = "EY"
replacement2 = "Eyjafjallajokull"
line2 = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."


###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###
marker2_1=line2.find(marker2)
marker2_2=line2.find(marker2[-1],marker2_1)+1
marker2_0=marker2_2-marker2_1
frist_quote2=line2[:marker2_1]
seconed_quote2=line2[(marker2_1)+marker2_0:]
replaced2 =frist_quote2+replacement2+seconed_quote2
print (replaced2)

# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.





