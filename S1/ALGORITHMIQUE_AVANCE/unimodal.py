lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 26, 25]

def maximum(lst):

    mid_point = (len(lst)//2)
    mid = lst[mid_point]
    right = lst[mid_point + 1]
    left = lst[mid_point - 1]
    
    print(lst)
    print("left : ",left, " / mid : ", mid, " / right : ", right)
    print()

    if left < mid > right:
        return mid, True

    if left > mid > right:
        if (mid_point - 1) < 3:
            return lst[:mid_point], False
        left_sub_lst = lst[:mid_point]
        return maximum(left_sub_lst)

    if left < mid < right:
        if (len(lst) - (mid_point + 1)) < 3:
            return lst[mid_point:], False
        right_sub_lst = lst[mid_point:]
        return maximum(right_sub_lst)


def max(lst):
   if len(lst) == 1:
       return lst[0]
   if len(lst) == 2:
       if lst[0] < lst[1]:
           return lst[1]
       else:
           return lst[0]
   lst, x = maximum(lst)
   print(lst)
   if x == True:
       return lst
   print(lst)
   if len(lst) == 1:
       return lst[0]
   if lst[0] < lst[1]:
       return lst[1]
   else:
       return lst[0]

print("maximum : ",max(lst))
