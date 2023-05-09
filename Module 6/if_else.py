if 'foo' in ['bar', 'foo', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

#One-Line if Statements
x=4
x=x+1 if x>40 else x-1
print(x)