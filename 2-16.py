while True:
    abc = input('What do you want to convert?')
    if abc =='bye':
             break
    elif abc =='2-16':
        while True:
            a = input('enter any binary number: ')
            if a == 'end':
                break
            else:
                for i in a:
                    if i not in '10':
                        print('Please enter 0 or 1!!!')
                        break
                    if a[0] == '0':
                        print('First number must be 1!!!')
                        break
                else:
                    if len(a)%4 ==0:
                        b,c,d,e,final_a = [],[],[],[],[]
                        for i in range(len(a)-1,-1,-4):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-4):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-4):
                            add3 = int(a[k])*4
                            d.append(add3)

                        for l in range(len(a)-4,-1,-4):
                            add4 = int(a[l])*8
                            e.append(add4)
                        
                        for x in range(len(b)-1,-1,-1):
                            add_final = b[x]+c[x]+d[x]+e[x]
                            if add_final == 10:
                                add_final = 'A'
                            elif add_final == 11:
                                add_final = 'B'
                            elif add_final == 12:
                                add_final = 'C'
                            elif add_final == 13:
                                add_final = 'D'
                            elif add_final == 14:
                                add_final = 'E'
                            elif add_final == 15:
                                add_final = 'F'
                            final_a.append(str(add_final))

                        #

                        final_a1 = ''.join(final_a)
                        print(final_a1)

                    elif len(a)%4 ==1:
                        b,c,d,e,final_a = [],[],[],[],[]
                        for i in range(len(a)-1,-1,-4):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-4):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-4):
                            add3 = int(a[k])*4
                            d.append(add3)

                        for l in range(len(a)-4,-1,-4):
                            add4 = int(a[l])*8
                            e.append(add4)

                        for x in range(0,len(c),1):
                            add_final = b[x]+c[x]+d[x]+e[x]
                            if add_final == 10:
                                add_final = 'A'
                            elif add_final == 11:
                                add_final = 'B'
                            elif add_final == 12:
                                add_final = 'C'
                            elif add_final == 13:
                                add_final = 'D'
                            elif add_final == 14:
                                add_final = 'E'
                            elif add_final == 15:
                                add_final = 'F'
                            final_a.append(str(add_final))

                        final_a.append(str(b[len(b)-1]))
                        for y in range(len(final_a)-1,-1,-1):
                            final_a.append(final_a[y])

                        for z in range(len(final_a)//2):
                            del final_a[0]
                            
                        #

                        final_a1 = ''.join(final_a)
                        print(final_a1)  

                    elif len(a)%4 ==2:
                        b,c,d,e,final_a = [],[],[],[],[]
                        for i in range(len(a)-1,-1,-4):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-4):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-4):
                            add3 = int(a[k])*4
                            d.append(add3)

                        for l in range(len(a)-4,-1,-4):
                            add4 = int(a[l])*8
                            e.append(add4)

                        for x in range(0,len(d),1):
                            add_final = b[x]+c[x]+d[x]+e[x]
                            if add_final == 10:
                                add_final = 'A'
                            elif add_final == 11:
                                add_final = 'B'
                            elif add_final == 12:
                                add_final = 'C'
                            elif add_final == 13:
                                add_final = 'D'
                            elif add_final == 14:
                                add_final = 'E'
                            elif add_final == 15:
                                add_final = 'F'
                            final_a.append(str(add_final))

                        final_a.append(str((b[len(b)-1])+(c[len(c)-1])))
                        for y in range(len(final_a)-1,-1,-1):
                            final_a.append(final_a[y])

                        for z in range(len(final_a)//2):
                            del final_a[0]
                            
                        #

                        final_a1 = ''.join(final_a)
                        print(final_a1)

                    elif len(a)%4 ==3:
                        b,c,d,e,final_a = [],[],[],[],[]
                        for i in range(len(a)-1,-1,-4):
                            add1 = int(a[i])*1
                            b.append(add1)

                        for j in range(len(a)-2,-1,-4):
                            add2 = int(a[j])*2
                            c.append(add2)

                        for k in range(len(a)-3,-1,-4):
                            add3 = int(a[k])*4
                            d.append(add3)

                        for l in range(len(a)-4,-1,-4):
                            add4 = int(a[l])*8
                            e.append(add4)

                        for x in range(0,len(e),1):
                            add_final = b[x]+c[x]+d[x]+e[x]
                            if add_final == 10:
                                add_final = 'A'
                            elif add_final == 11:
                                add_final = 'B'
                            elif add_final == 12:
                                add_final = 'C'
                            elif add_final == 13:
                                add_final = 'D'
                            elif add_final == 14:
                                add_final = 'E'
                            elif add_final == 15:
                                add_final = 'F'
                            final_a.append(str(add_final))

                        final_a.append(str((b[len(b)-1])+(c[len(c)-1])+(d[len(d)-1])))
                        for y in range(len(final_a)-1,-1,-1):
                            final_a.append(final_a[y])

                        for z in range(len(final_a)//2):
                            del final_a[0]
                            
                        #

                        final_a1 = ''.join(final_a)
                        print(final_a1)  

    elif abc =='16-2':
        while True:
            a = input('enter any hexadecimal number: ')
            if a == 'end':
                break
            else:
                for i in a:
                    if i not in '0123456789ABCDEF':
                        print('Please enter  0~9 or A~F!!!')
                        break
                    if a[0] == '0':
                        print("First number can't be 0!!!")
                        break
                else:
                    ans = []
                    for i in range(len(a)-1,-1,-1):
                        if a[i] == '0':
                            ans.append('0000')
                        elif a[i] == '1':
                            ans.append('0001')
                        elif a[i] == '2':
                            ans.append('0010')
                        elif a[i] == '3':
                            ans.append('0011')
                        elif a[i] == '4':
                            ans.append('0100')
                        elif a[i] == '5':
                            ans.append('0101')
                        elif a[i] == '6':
                            ans.append('0110')
                        elif a[i] == '7':
                            ans.append('0111')
                        elif a[i] == '8':
                            ans.append('1000')
                        elif a[i] == '9':
                            ans.append('1001')
                        elif a[i] == 'A':
                            ans.append('1010')
                        elif a[i] == 'B':
                            ans.append('1011')
                        elif a[i] == 'C':
                            ans.append('1100')
                        elif a[i] == 'D':
                            ans.append('1101')
                        elif a[i] == 'E':
                            ans.append('1110')
                        elif a[i] == 'F':
                            ans.append('1111')
                            
                    if a[0] == '1':
                        del ans[len(ans)-1]
                        ans.append('1')
                    elif a[0] == '2':
                        del ans[len(ans)-1]
                        ans.append('10')
                    elif a[0] == '3':
                        del ans[len(ans)-1]
                        ans.append('11')
                    elif a[0] == '4':
                        del ans[len(ans)-1]
                        ans.append('100')
                    elif a[0] == '5':
                        del ans[len(ans)-1]
                        ans.append('101')
                    elif a[0] == '6':
                        del ans[len(ans)-1]
                        ans.append('110')
                    elif a[0] == '7':
                        del ans[len(ans)-1]
                        ans.append('111')
                        
                    for j in range(len(ans)-1,-1,-1):
                        ans.append(ans[j])

                    for k in range(len(ans)//2):
                        del ans[0]

                   

                    final_ans = ''.join(ans)
                    print(final_ans)

