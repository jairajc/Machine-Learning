def nestedConditional(x):
    if x>0 and x<10:
        print "Single Digit Positive Number"
    elif x>11 and x<99:
        print "Double Digit Postive Number"
    elif x>=100:
        print "Invalid Input"
    elif x<0:
        print "Negative Number"
nestedConditional(100)
