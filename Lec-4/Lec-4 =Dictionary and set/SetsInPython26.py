# set is the collection of unordered( no index) values....
# Each elements in a set must be unique and immutable... meaning , set is mutable...

# duplicated elements hudaina means strings , numbers , int , etc yek patak matra store garna milca

set1 = {2,3,4,5,6,7,2,3,"Bibek","lamichhane","Bibek"}   # repeated bhayeko elements is only stored once so , it resolves to {2,3,4,5,6,7,bibek,lamichhane}
print(len(set1) ,"\n" ,set1) 


# if we wanna make empty set , how to make?
Emp_set = {} # This is wrong because this is an empty dictionary not a set ..hahahah...
Emp_set = set()  # This is an proper way of writing empty set in python..and  syntax for empty set is also this

print(Emp_set.add("bibek"))
print(Emp_set)