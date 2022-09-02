def gstCalc(invValue,gstp):
    print("Your Invoice value is", invValue)
    print("Your GST Amount Is", (invValue*gstp)/100)
    print("Your GST Invoice Amount Is", invValue + (invValue*18)/100)

gstCalc(200,18)