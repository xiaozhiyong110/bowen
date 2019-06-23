def read_data():
    data=[]
    with open(r'C:\Users\xiaozy\PycharmProjects\untitled\diesheng\data\data1.txt','r',encoding='utf-8') as fd:
        d=fd.readlines()
        for i in d:
            data.append(i.replace('\n','').split(','))
    return data