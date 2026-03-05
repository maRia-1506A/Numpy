import numpy as np

number= np.array([1,2,3,4,5,6,7,8,9,10])
indices= [0,2,4]

# where condition 
where_result= np.where(number>5)
print(where_result)
print("Greater than 5: ", number[where_result])


# where condition 1 
'''if(number > 5) {
    number*4
} else {
    number
}'''

condition= np.where(number>5, number*4, number)
print("\n",condition)
