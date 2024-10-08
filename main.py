calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info (string):
    stroka = str (string)
    result = (len (stroka), stroka.upper (), stroka. lower ())
    count_calls()
    return result

def is_contains (string, list_to_search):
    count_calls()
    for i in range (len (list_to_search)):
        if list_to_search [i] == string:
            return True
        else:
            return False

print (string_info('lemon'))
print (string_info('green tea'))
print (is_contains ('apple', ['banana', 'lemon', 'ananas']))
print (is_contains ('milk', ['milk', 'Tea', 'coffee']))

print (calls)

