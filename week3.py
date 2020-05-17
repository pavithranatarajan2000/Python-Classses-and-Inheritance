#WEEK3



#question1


'''
The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
'''


import test
list=[1]
def mySum():
    return list[0]
print(mySum())
test.testEqual(mySum(),6)



#Multiple choice questions

'''
Which of the following cases fail for the mySum function?

A. an empty list*
B. a list with one item
C. a list with more than one item*

Answer:A,C



test-4-2: Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?

A. Yes
B. No

Answer:B

'''

#question2
'''
The class Student is supposed to accept two arguments in its constructor:
A name string

An optional integer representing the number of years the student has been at Michigan (default:1)

Every student has three instance variables:
self.name (set to the name provided)

self.years_UM (set to the number of years the student has been at Michigan)

self.knowledge (initialized to 0)

There are three methods:
.study() should increase self.knowledge by 1 and return None

.getKnowledge() should return the value of self.knowledge

.year_at_umich() should return the value of self.years_UM

There are one or more errors in the class. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
'''


import test
class Student:
    def __init__(self,name,years_UM):
        self.name=name
        self.years_UM=8
        self.knowledge=0
    def study(self):
        self.knowledge=self.knowledge
    def getKnowledge(self):
        return None
    def year_at_umitch(self):
        return self.years_UM
a=Student('pavi',10)
a.study()
test.testEqual(a.getKnowledge(),1)
test.testEqual(a.years_UM,10)


#Multiple choice questions

'''
Which of the following cases fail for the Student class?

A. the method study does not return None
B. the optional integer in the constructor is not optional
C. the attributes/instance variables are not correctly assigned in the constructor
D. the method study does not increase self.knowledge
E. the method year_at_umich does not return the value of self.years_UM

Answer:C,D


test-4-4: Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?

A. Yes
B. No

Answer:A

'''






