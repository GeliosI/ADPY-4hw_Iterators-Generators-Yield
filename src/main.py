class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def _get_flat_list(self, nested_list):  
        for elem in nested_list:
            if type(elem) == list:
                yield from self._get_flat_list(elem)                
            else:
                yield elem
            
    def __iter__(self):
        self.flat_list_gen = self._get_flat_list(nested_list)
        return self

    def __next__(self):
        return next(self.flat_list_gen)


def flat_generator(nested_list): 
    for elem in nested_list:
        if type(elem) == list:
            yield from flat_generator(elem)                
        else:
            yield elem


if __name__ == "__main__":
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    
    print('[+] FlatIterator result:')
    print('\t', end=' ')
    for item in FlatIterator(nested_list):
        print(item, end=' ')

    print('\n\n[+] list comprehension result:')
    flat_list = [item for item in FlatIterator(nested_list)]
    print('\t', flat_list)

    print('\n[+] generator result:')
    print('\t', end=' ')
    flat_get = flat_generator(nested_list)

    for item in flat_get:
        print(item, end=' ')

    print('\n')