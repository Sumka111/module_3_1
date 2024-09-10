calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    a = (len(string))
    b = (string.upper())
    c = (string.upper().lower())
    return a, b, c
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [to.lower() for to in list_to_search]
    string = string.lower()
    if string in list_to_search:
        return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)