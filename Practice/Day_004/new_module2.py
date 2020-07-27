import sys
def say_hello(msg):
    return 'Hello ! ' + msg

def main():
    # msg = sys.argv[1]
    # if msg is None:
    #     print('enter msg')
    # else:
    #     print(say_hello(msg))
    
    # >> command line argument

    print(say_hello('python is so easy to learn!'))

# main()

if __name__ == '__main__':
    ### This make avoid the call main() when this file is imported ##
    print('Execute directly')
    main()
else:
    print('Execute with import')
