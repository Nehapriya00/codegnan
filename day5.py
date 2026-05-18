'''
#sets: a set is a collection of unique and unordered elements.duplicate values are not allowed. items are not stored in index order.it is represented in {}
any={1,2,2,4,5,5,6}
print(any)

#methods
#union(): if we consider 2 sets by using union it will combine both the sets elements.without printing the common elements.
#syntax:variable_name.union(variable2)
any={1,2,5,3,3,4}
an={78,66}
print(any|an)
print(any.union(an))

#intersection():to get the common elements for both the sets
#syntax:variable_name.intersection(variable2)
any={4,6,5,5,2,1}
an={50,6,1,9}
print(any & an)
print(any.intersection(an))

#difference(): to get different values from the set
#syntax:variable_name.differnce(variable2)
any={4,5,6,8}
an={5,6,9}
print(any-an)
print(any.difference(an))

#add(): to add new element into set
#syntax:variable_name.add(element)
any={1,2,3,3,4}
any.add(41)
print(any)

#update(): to add multiple items to the set
#syntax:variable_name.update([elements])
any={2,3,4,5,5}
any.update([41,60])
print(any)
'''
any={2,3,4,5,5}
print(min(any))
print(sum(any))
print(len(any))

#remove(): it is used to remove or delete element for the set but it through error if the element is not in the set
#syntax: variable_name.remove(element)
any={7,5,8,8,2}
any.remove(8)
print(any)

#discard(): it is used to remove or delete element for the set but it will not through error if the element is not in the set
#syntax: variable_name.discard(element)
any={7,5,8,8,2}
any.discard(8)
print(any)
