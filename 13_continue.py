# Continue Statement
# continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.

for i in range(1,10):
    if i<5:
        continue
    else:
        print(i)

# Explanation:
# When value of i becomes less than 5 it skips the block and executes next iteration
# Eg: When i = 1
# i less than 5 is true
# then it will skip to print and force to execute next loop
# eg: when i = 4
# i less than 4 is true
# so, it will force to next loop changing the value of loop to 5
# so i becomes 5
# as, 5 less than 5 is false
# it moves to else part