# from functools import reduce
#
# initial_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
# flattened_list = reduce(lambda x, y: x + y, initial_list)
#
# print(flattened_list)
#
#
# flattened_list=list(filter(lambda x : x%2==0 , flattened_list))
# print(flattened_list)
# list_words=["as","fd","aerr","werd"]
# list_words=list(filter(lambda x : "a" in x,list_words))
# print(list_words)
#
#
# list1=[1,2,3,4,5,6,7]
# list2=[1,2,3,4,5]
# list3=[1,2,3,4,5,6,7,8,9,0]
# lists_for_zip_compr=[i for i in zip(list2,list1)]
# list_our=[list3,list2,list1]
# max_lenth=len(max(list_our,key=len))
# for i in range(len(list_our)):
#     if  len(list_our[i])<max_lenth:
#         list_our[i]=list_our[i]+[0]*(max_lenth-len(list_our[i]))
# print(list_our)



#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610


def fibonachi(point,start=0,second=1,count=1):
    if point==count:
        return start
    return fibonachi(point,start=second,second=start+second,count=count+1)

# выводит нужный член ряда фибоначи



class PlaceHolder:


    def __init__(self,name):
        self.name=name

    def return_name(self):
        return self.name





