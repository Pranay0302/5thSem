# temperature scales K F C

# formulas

# F = 1.8C + 32

# K = C + 273.15

def c2f(c):
    return ((c*1.8) + 32)

def f2c(f):
    return ((f-32)/1.8)

def c2k(c):
    return (c+273.15)

def k2c(k):
    return (k-273.15)

def f2k(f):
    return c2k(f2c(f))

def k2f(k):
    return c2f(k2c(k))

select = 'y'

while(select == 'y'):
    op = input('1. c2f 2. f2c 3. k2c 4. c2k 5. k2f 6. f2k \n')
    if(op):
        if(op == '1'):
            x = float(input('enter temperature in celsius: \t'))
            res = c2f(x)
            print(f'celsius: {x} & fahrenheit: {res}')
        elif(op == '2'):
            x = float(input('enter temperature in fahrenheit: \t'))
            res = f2c(x)
            print(f'fahrenheit: {x} & celsius: {res}')
        elif(op == '3'):
            x = float(input('enter temperature in kelvin: \t'))
            res = k2c(x)
            print(f'kelvin: {x} & celsius: {res}')
        elif(op == '4'):
            x = float(input('enter temperature in celsius: \t'))
            res = c2k(x)
            print(f'celsius: {x} & kelvin: {res}')
        elif(op == '5'):
            x = float(input('enter temperature in kelvin: \t'))
            res = k2f(x)
            print(f'kelvin: {x} & fahrenheit: {res}')
        elif(op == '6'):
            x = float(input('enter temperature in fahrenheit: \t'))
            res = f2k(x)
            print(f'fahrenheit: {x} & kelvin: {res}')
        else:
            print('bad input')
            exit()
