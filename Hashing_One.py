'''
Given an array A. You have some integers given in the array B.
For the i-th number, find the frequency of B[i] in the array A and 
return a list containing all the frequencies.
for Eg:
A = [1, 2, 1, 1]
B = [1, 2]
Output 1: [3, 1]
'''
class solution:
    def __init__(self,A,B):
        self.A = A
        self.B = B
        self.C = {}
        self.result = []
    def build_count_dict(self):
        for ele in self.A:
            if ele in self.C:
                self.C[ele]+= 1
            else:
                self.C[ele] = 1
    def build_result(self):
        for ele in self.B:
            if ele in self.C:
                self.result.append(self.C[ele])
            else:
                self.result.append(0)
    def process_list(self):
        self.build_count_dict()
        self.build_result()
        return self.result
    
A = [1,2,1,1]
B= [1,2,3]
processor = solution(A,B)
result  = processor.process_list()
print(result)
'''
Given an array A of N integers, return the number of unique elements in the array.
A = [3, 4, 3, 6, 6]
output: 3
'''
A = [3,4,3,6,6]
B = {}
C = []
for ele in A:
    if ele in B:
        B[ele]+=1
    else:
        B[ele] = 1
print(B)
print(B.__len__())