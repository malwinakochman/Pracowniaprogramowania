class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_col_with(array):
        count = 0
        for c in array:
            count += 1
            if count != len(array):
                print(c, end = ',')
            else:
                print(c, end = '')
            
    
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_col_with(my_array)
