# f=open('test.txt','r')
# print(f.name)
# f.close()

#context manager "with" keyword
# with open('test.txt','r',encoding='utf-8')as f:
#     #f_contents=f.read()
#     #f_contents=f.readlines()
#     #f_contents=f.readline()
#     size_to_read=150
#     f_contents=f.read(size_to_read)
#     #print(f.tell())
#     while len(f_contents)>0:
#         print(f_contents,end='')
#         f_contents=f.read(size_to_read)


with open('test.txt','r',encoding='utf-8') as rf:
    with open('copy.txt','w',encoding='utf-8') as wf:
        chunk_size=2048
        rf_contents=rf.read(chunk_size)
        while len(rf_contents)>0:
            wf.write(rf_contents)
            rf_contents=rf.read(chunk_size)