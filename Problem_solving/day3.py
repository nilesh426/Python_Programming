# bill=[3,10,2,9]
# print((sum(bill)-bill[1])/2)


unsorted=['1','200','150','3']
for i in range(len(unsorted)):
    for j in range(len(unsorted)):
        if unsorted[i] > unsorted[j]:
            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]

print(unsorted)           
        
