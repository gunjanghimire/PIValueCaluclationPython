#Calculate Value of PI using the Neelkantha method to nth digit using upto 50 trailing digits
j = 3.0
k=1
for i in range(2, 4000000, 2): #Change the Desired End Step to get a better nth value
    k = k+1
    if k % 2 ==0:
        j = j+ 4/(i*(i+1)*(i+2))
    else:
        j = j- 4/(i*(i+1)*(i+2))
kaggle = input('Enter value of n upto which you want to display the value of PI:')
a = '%.'+kaggle+'f'
print (a%(j))