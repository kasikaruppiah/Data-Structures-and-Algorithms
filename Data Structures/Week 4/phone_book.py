# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    m = 10 ** 7
    contacts = [None] * m
    a = 34
    b = 2
    x = 1482567
    p = 10000019
    for cur_query in queries:
        h = (a * cur_query.number + b) % p
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if contacts[h] != None:
                contacts[h].name = cur_query.name
            else:
                contacts[h] = cur_query
        elif cur_query.type == 'del':
            if contacts[h] != None:
                contacts[h] = None
        else:
            response = 'not found'
            if contacts[h] != None:
                response = contacts[h].name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

