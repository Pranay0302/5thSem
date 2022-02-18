def _max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = _max(list[1:])
        return m if m > list[0] else list[0]

def check():
    try:
        ip = eval(input('enter numbers: \t'))
        x = _max(ip)
        print(f'max number is: {x}')
    except:
        print('bad input, make sure you add comma seperated numbers')

check()
