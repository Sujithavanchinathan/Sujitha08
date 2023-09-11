# leaf year

"""




"""
def isleafyear(year):
  if(year % 4 == 0 and year % 100 !=0):
    return True
  else:
    return False

year = int(input("enter a year:"))

if isleafyear (year):
  print('{} is not leaf year.'.format(year))
  
  


  
  