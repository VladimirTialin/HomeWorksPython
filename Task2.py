nums = [1, 5, 2, 3, 4, 6, 1, 7]
temp=[]
[temp.append(i) for i in nums if i not in temp]
temp=sorted(temp)
print(temp)
for i in range(len(temp)):
  if temp[i+1]-temp[i]!=1:
      maxIndex=temp[i]
      break
  else:
      maxIndex=temp[-1]
result=[temp[0],maxIndex]
print(result)