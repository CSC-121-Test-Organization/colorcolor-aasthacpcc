print('==================== numeric input for color choice=============\n\n')
print('Color Choices are: \n'
      '\t 1.  Red \n'
      '\t 2.  Blue \n' 
      '\t 3.  Yellow \n')

#Get Input Information
first_color = int(input('First color choice> '))
second_color = int(input('Second color choice> '))

print('\n ==================== program output: ==================== \n')

#evaluate color combinations
if (first_color == 1 or second_color == 1) and (first_color == 2 or second_color == 2):
    print('resulting color is purple \n')
elif (first_color == 1 or second_color == 1) and (first_color == 3 or second_color == 3):
    print('resulting color is orange \n')
elif (first_color == 2 or second_color == 2) and (first_color == 3 or second_color == 3):
    print('resulting color is green \n')
elif (first_color == second_color):
    print('COLOR 1 AND COLOR 2 CANNOT BE THE SAME\n')
else:
    #check to see which colors are invalid
    invalid_colors1 = "Color 1" if (first_color < 1 or first_color > 3) else ""
    invalid_colors2 = "Color 2" if (second_color < 1 or second_color > 3) else ""
    print(f'{invalid_colors1} {invalid_colors2} CHOICE INVALID - PROGRAM ENDING! \n')
