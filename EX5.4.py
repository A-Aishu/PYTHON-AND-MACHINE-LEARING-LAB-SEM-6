y =int(input())
if y % 4 == 0 :
    if y % 100 == 0:
        if y % 400 == 0:
            print("%d is a leap year"%y)
        else :
           print("%d is not a leap year"%y)
    else :
       print("%d is a leap year"%y)
else :
  print("%d is not a leap year"%y)
