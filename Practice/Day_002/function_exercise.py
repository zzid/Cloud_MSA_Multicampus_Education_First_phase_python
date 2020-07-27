def connect(server,port):
    # pass # this mean, teporary!
    return 'Conneted - http://{}:{}'.format(server, port)


def my_average(prices):
    return int(sum(prices) / len(prices))

def times(a= 10, b= 20): # default parameters
    return a+b
'''
*p : tuple type parameter
**p : dict type parameter

>>>>>>>>>>>>>> # of parameter can be variable

'''
def var_param_test(*p):
    return p
def var_param_test2(**p):
    for x,v in p.items():
        print(x,v)
############################################
def kwargs_test_3(one, two, *args, **kwargs):
    print('one+ two : ', one + two)
    print(sum(args))
    print(kwargs)
############################################

def swap(a,b): ########### returning multiple parameters #######
    return b,a
def swap2(a,b):
    return b,a,a,b
################################################################

def main():
    prices = [1000,3000, 2500, 450]
    result = my_average(prices)
    print(result)

    result1 = connect('server.com', '8080')
    print(result1)
    
    result2 = connect(port= '1017', server = 'another.com')
    print(result2)

    print(times()) # 30
    print(times(1,2)) # 3
    print(times(1)) # 21

    print(var_param_test(1,2,3,4,5))
    print(var_param_test(19,20))
    print(var_param_test(27,)) # (27,)
    print(var_param_test(27)) # (27,)
    var_param_test2(a=1, b=2,c=3,d=4,e=5,f=6)
    # dict_test = {}
    # dict_test['a'] = 'b'
    # dict_test['c'] = 'd'
    # var_param_test2(dict_test)
    ## error
    kwargs_test_3(1,2,3,4,5,6, a=1,b=3) # one + two : 3 \n 18

    print(swap(1,2)) # (2,1) >> tuple
    print(swap2(1,2)) # (2,1,2,1) >> tuple


main()