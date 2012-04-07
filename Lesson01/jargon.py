lenght = int(raw_input("Enter length: "))
width = int(raw_input("Enter width: "))
screenWidth = 80
padding = ' ' * ((screenWidth - lenght) / 2)
topRow = padding + '+' + '-' * (lenght - 2) + '+' 
fillRows = padding + '|' + ' ' * (lenght - 2) + '|' 


print topRow
print fillRows * (width - 2)
print topRow