# UCP HW: Arrays & Strings
def isStringPermutation(s1: str, s2: str)->bool:
    # Is s1 a permutation of s2?
    # Ex. s1 = "asdf", s2 = "fsda" -> True
    list1 = sorted(s1)
    list2 = sorted(s2)
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def pairsThatEqualSum(inputArray: list, targetSum: int)->list:
    # What pairs equal targetSum?
    # Ex. inputArray = [1, 2, 3, 4, 5], targetSum = 5 -> ([(1,4)], [(2,3)]
    inputArray.sort()
    leftIndex = 0
    rightIndex = len(inputArray)-1
    outputArray = []
    while (leftIndex < rightIndex):
        currentSum = inputArray[leftIndex] + inputArray[rightIndex]
        if currentSum == targetSum:
            outputArray.append((inputArray[leftIndex], inputArray[rightIndex]))
            rightIndex -= 1
            leftIndex += 1 
        elif currentSum > targetSum:
            rightIndex -= 1
        else:
            leftIndex += 1
    return outputArray

def main():
    # 1
    str1 = input("String 1: ")
    str2 = input("String 2: ")
    print("String 1:", str1)
    print("String 2:", str2)
    print(str1, "is a permutation of", str2 + ":", isStringPermutation(str1, str2))
    
    # 2
    inputArr = [int(elem) for elem in input("Integer Array: ").split()]
    targ = int(input("Target Sum: "))
    print(pairsThatEqualSum(inputArr, targ))
    
main()
