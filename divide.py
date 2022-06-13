with open('./data/BIO_test.utf8','r',encoding='utf8')as f:
    with open('msra_train.txt', 'w', encoding='utf8')as train:
        with open('msra_test.txt', 'w', encoding='utf8')as test:
            # train_set=[]
            # test_set=[]
            content = f.readlines()
            for i,line in enumerate(content):
                line = line.replace('\n', '')
                if i < 124061:
                    train.write(line + '\n')
                else:
                    test.write(line + '\n')

        # train_set=content[:124061]
        # test_set=content[124062:]
        # print(train_set)
        # print(test_set)
    '''
with open('msra_train.txt','w',encoding='utf8')as f:
    train=str(train_set)
    train=
    f.write(str(train_set))
    f.close()
with open('msra_test.txt','w',encoding='utf8')as f:
    f.write(str(test_set))
    f.close()'''





