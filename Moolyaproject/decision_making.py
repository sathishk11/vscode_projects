#if else
marks=90
if marks>=90:
    print("allowed games")
elif marks>=70 and marks <=90:
    print("study hard")
else:
    print("lathithy charge")

l=[20,40,30,60,90]
max_num=l[0]
for x in l: #iterator
    if x>max_num:
        max_num=x

print("The largest num is:",max_num)

m=[20,40,30,60,90,10]
min_num=m[0]
for x in m:
    if x<min_num:
        min_num=x

print("The smallest num is:",min_num)

a=[12,45,32,89]
print(max(a))