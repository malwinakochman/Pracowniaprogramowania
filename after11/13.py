class Arrays():
    
    @staticmethod
    def creating_array(number_of_array_elements, value_of_array_elements):
        array1 = []
        for i in range(0, number_of_array_elements):
            array1.append(value_of_array_elements)
        return array1
            
    @staticmethod
    def create_random_array(number_of_array_elements, value_from, value_to):
        import random
        array2 = []
        for i in range(0, number_of_array_elements):
            x = random.randrange(value_from, value_to+1)
            array2.append(x)
        return array2
    
    @staticmethod
    def determines_array(array, value_from, value_to):
        array3 = []
        for i in array:
            if i >= value_from and i<= value_to:
                array3.append(i)
        return array3
        
#program:
array_10 = Arrays.creating_array(10,4)
array_20 = Arrays.create_random_array(5, -7, 8)
count = 0
for i in range(-1,2):
    for x in array_20:
        if x == i:
            count += 1
            break
            
print(array_10)
print(" ")
print(array_20)
print(f"Count contained in array: {count}")

    
            
#number_of_array_elements = 5
#value_of_array_elements = 1
#value_from = 10
#value_to = 500
#array = [10, 24, 765, 999, 101, 2, 13, 1, 888, 435, 500]
#print(Arrays.creating_array(number_of_array_elements, value_of_array_elements))
#print(" ")
#print(Arrays.create_random_array(number_of_array_elements, value_from, value_to))
#print(" ")
#print(Arrays.determines_array(array, value_from, value_to))