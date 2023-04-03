def matchingStrings(strings, queries):
    # Write your code here
    res=[]
    for item in queries:
        res.append(strings.count(item))
    return res

if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc']
    queries = ['ab',  'abc', 'bc']
    result = matchingStrings(strings, queries)
    print(result)