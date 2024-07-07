calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contain(string, list_to_search):
    count_calls()
    return any(i.lower() == string.lower() for i in list_to_search)

print(string_info('Denis'))
print(string_info('Ekaterina'))
print(is_contain('Denis', ['Irina', 'iVan', 'deNiS']))
print(is_contain('Bmw', ['Audi', 'Volvo', 'Zeekr']))
print(calls)