array=['a','ab','b','bb','c','cc','d','db','e','eb','f','fb','g','gb','h','hb',
       'i','ib','j','k','kb','l','lb','m','mb','n','nb','o','oo','p','pb','q','qb','r','rb','s','ss','t','tb','u'
       ,'uu','v','w','x','y','yb','z','0','1','2','3','4','5','6','7','8','9']
for i in range(1, 58):

    print('item {')
    print('   id: {}'.format(i))
    print("   name: '{}' ".format(array[i-1]))
    print('   display_name: " "\n}')


