# Tu ek wedding planner hai. Do alag-alag guest lists tere paas hain — dono already sorted alphabetically (by first letter priority, simplify kar ke soch numbers ke roop mein). Tujhe dono lists ko merge karke ek hi final combined guest list banani hai, jo bhi sorted order mein ho — taaki tu ek single seating chart bana sake.



def merge_sorted_lists(arr1,arr2):
    final_list=[]
    n = max(len(arr1), len(arr2))
    
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            final_list.append(arr1[i])
            i += 1
        else:
            final_list.append(arr2[j])
            j += 1
        
    return final_list + arr1[i:] + arr2[j:]
    

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list1, list2))