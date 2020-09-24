lst = [1, 3, 4, 5, 8,20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3,  2, 1, 0]

def maximum(lst):

    mid_point = (len(lst)//2)
    mid = lst[mid_point]
    right = lst[mid_point + 1]
    left = lst[mid_point - 1]
    
    print(lst)
    print("left : ",left, " / mid : ", mid, " / right : ", right)
    print()

    if left < mid > right:
        return mid

    if left > mid > right:
        if (mid_point - 1) < 3:
            return lst[:(mid_point - 1)]
        left_sub_lst = lst[:mid_point]
        return maximum(left_sub_lst)

    if left < mid < right:
        if (len(lst) - (mid_point + 1)) < 3:
            return lst[(mid_point + 1):]
        right_sub_lst = lst[mid_point:]
        return maximum(right_sub_lst)


def max(lst):
   lst = maximum(lst)
   if len(lst) == 1:
       return lst[0]
   if lst[0] < lst[1]:
       return lst[1]
   else:
       return lst[0]

print("maximum : ",max(lst))
