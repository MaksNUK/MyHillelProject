from time import perf_counter

def timer(func):
    def function(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start
        print(f'Duration time : {duration} seconds')
        return result
    return function

def array3():
    lenth = int(input('Input lenth array'))
    arrray_by_input = [x*3 for x in range(1, lenth + 1)]
    return print(arrray_by_input[::-1])

def triangular_number_generator():
    n = int(input())
    triangular_number = int(n*(n+1)/2)
    return print(triangular_number)

def skip(func):
    def get_parameter(*args):
        tuple_real_parameters = func(*args)
        print(f"Not returned real_parameters {tuple_real_parameters}")
        fake_parameter = 'This is fake parameter'
        return print(f"Reterned fake parameter -> {fake_parameter}")
    return get_parameter

@timer
@skip
def test():
    test_parameter = 2**5
    test_parameter2 = 2**2
    return test_parameter, test_parameter2

if __name__=="__main__":
    test()

