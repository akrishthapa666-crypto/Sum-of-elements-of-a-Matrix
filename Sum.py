rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns:"))

matrix=[]
for i in range(rows):
  row=list(map(int,input().split()))
  matrix.append(row)

sum=0
for i in range(rows):
  for j in range(cols):
    sum+=matrix[i][j]

print("sum=",sum)
