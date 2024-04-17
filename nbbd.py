import matplotlib.pyplot as plt 
from blood_bank_base import *
import time





def login_as_admin():
    global request
    sudopin=0000
    givenpin=float(input('Enter pin :'))
    if givenpin==sudopin:
        while True:
            print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            time.sleep(0.1)
            print('|                            WELCOME                              |')
            time.sleep(0.1)
            print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            time.sleep(0.1)
            print('1.update storage status')
            time.sleep(0.1)
            print('2.view requests')
            time.sleep(0.1)
            print('3.log off')

            r=float(input('Select [1~3]:'))
            if r==1:

                print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
                time.sleep(0.1)
                print('|Which blood group do you want to update ==>                      |')
                time.sleep(0.1)
                print('|1.A+                                                             |')
                time.sleep(0.1)
                print('|2.B+                                                             |')
                time.sleep(0.1)
                print('|3.O+                                                             |')
                time.sleep(0.1)
                print('|4.A-                                                             |')
                time.sleep(0.1)
                print('|5.B-                                                             |')
                time.sleep(0.1)
                print('|6.O-                                                             |')
                time.sleep(0.1)
                print('|7.Ab+                                                            |')
                time.sleep(0.1)
                print('|8.Ab-                                                            |')
                time.sleep(0.1)
                print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
                print()
                s=float(input('Select [1~8]: '))
                if s==1:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of A+ in the storage: '))
                    time.sleep(0.1)
                    bank['A+']=existing_amt
                    print('updated successfully!!!')

                elif s==2:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of B+ in the storage: '))
                    bank['B+']=existing_amt
                    time.sleep(0.1)
                    print('Updated successfully!!!')

                elif s==3:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of O+ in the storage: '))
                    time.sleep(0.1)
                    bank['O+']=existing_amt
                    print('Updated successfully!!!')

                elif s==4:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of A- in the storage: '))
                    time.sleep(0.1)
                    bank['A-']=existing_amt
                    print('Updated successfully!!!')

                elif s==5:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of B- in the storage: '))
                    time.sleep(0.1)
                    bank['B-']=existing_amt
                    print('Updated successfully!!!')

                elif s==6:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of O- in the storage: '))
                    time.sleep(0.1)
                    bank['O-']=existing_amt
                    print('Updated successfully!!!')

                elif s==7:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of Ab+ in the storage: '))
                    time.sleep(0.1)
                    bank['Ab+']=existing_amt
                    print('Updated successfully!!!')

                elif s==8:
                    time.sleep(0.1)
                    existing_amt=float(input('What is the existing amount of Ab- in the storage: '))
                    time.sleep(0.1)
                    bank['Ab-']=existing_amt
                    print('Updated successfully!!!')

        
            elif r==2:
                time.sleep(0.1)
                for a in request.keys():
                    print('=> '+str(a)+'of about '+str(request[a])+' mililitres has been requested.')
                    time.sleep(0.1)
                print('1. Accept')
                time.sleep(0.1)
                print('2. Reject')
                time.sleep(0.1)

                moody=int(input('Select [1~2]: '))
                if moody==1:

                    for a in request.keys():
                        rem=bank[a]-request[a]
                        bank[a]=rem
                    time.sleep(0.1)
                    print('the request has been fulfilled.')
                    request={}
                elif moody==2:
                    request={}
                    time.sleep(0.51)
                    print('That is Cruel.....')
                    time.sleep(0.1)
                else:
                    print()
        
            elif r==3:
                break
            
            
            else:
                time.sleep(0.1)
                print('Invalid Choice')
    
    else:
        time.sleep(0.1)
        print('Invalid Password!!!')



def login_as_donor():
    time.sleep(0.1)
    given_donor=input('Enter your name: ')


    if given_donor in userbase:
        time.sleep(0.1)
        given_pin=float(input('Enter your Pin: '))
        if given_pin==userbase[given_donor]:
            print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            time.sleep(0.1)
            print('|                            WELCOME                              |')
            time.sleep(0.1)
            print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            time.sleep(0.1)
            time.sleep(0.1)
            print('1.Donate Blood')
            time.sleep(0.1)
            print('2.Request Blood')
            time.sleep(0.1)
            s=float(input('Select [1~2]: '))
            if s==1:
                print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
                time.sleep(0.1)
                print('|Which blood group do you want to donate ==>                    |')
                time.sleep(0.1)
                print('|1.A+                                                           |')
                time.sleep(0.1)
                print('|2.B+                                                           |')
                time.sleep(0.1)
                print('|3.O+                                                           |')
                time.sleep(0.1)
                print('|4.A-                                                           |')
                time.sleep(0.1)
                print('|5.B-                                                           |')
                time.sleep(0.1)
                print('|6.O-                                                           |')
                time.sleep(0.1)
                print('|7.Ab+                                                          |')
                time.sleep(0.1)
                print('|8.Ab-                                                          |')
                time.sleep(0.1)
                print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')

                print()

                r=float(input('Select [1~8]: '))
                time.sleep(0.1)
                if r==1:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['A+']=bank['A+']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)

                elif r==2:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['B+']=bank['B+']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)

                elif r==3:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['O+']=bank['O+']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)

                elif r==4:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['A-']=bank['A-']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)
                
                elif r==5:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['B-']=bank['B-']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)

                elif r==6:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['O-']=bank['O-']+amt
                    print('Donated successfully!!!') 
                    time.sleep(0.1)

                elif r==7:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['Ab+']=bank['Ab+']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)

                elif r==8:
                    amt=float(input('How much do you want to donate: '))
                    time.sleep(0.1)
                    bank['Ab-']=bank['Ab-']+amt
                    print('Donated successfully!!!')
                    time.sleep(0.1)
            
                else:
                    time.sleep(0.1)
                    print('Invalid Choice!!!')
            


            elif s==2:
                print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
                time.sleep(0.1)
                print('|Which blood group do you want to request ==>                   |')
                time.sleep(0.1)
                print('|1.A+                                                           |')
                time.sleep(0.1)
                print('|2.B+                                                           |')
                time.sleep(0.1)
                print('|3.O+                                                           |')
                time.sleep(0.1)
                print('|4.A-                                                           |')
                time.sleep(0.1)
                print('|5.B-                                                           |')
                time.sleep(0.1)
                print('|6.O-                                                           |')
                time.sleep(0.1)
                print('|7.Ab+                                                          |')
                time.sleep(0.1)
                print('|8.Ab-                                                          |')
                time.sleep(0.1)
                print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')

                r=float(input('Select [1~8]: '))
                time.sleep(0.1)
                how_much=float(input('how much:'))
                time.sleep(0.1)

                if r==1 and bank['A+']>=how_much:
                    request['A+']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==2 and bank['B+']>=how_much:
                    request['B+']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==3 and bank['O+']>=how_much:
                    request['O+']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==4 and bank['A-']>=how_much:
                    request['A-']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==5 and bank['B-']>=how_much:
                    request['B-']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==6 and bank['O-']>=how_much:
                    request['O-']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==7 and bank['Ab+']>=how_much:
                    request['Ab+']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                elif r==8 and bank['Ab-']>=how_much:
                    request['Ab-']=how_much
                    time.sleep(0.1)
                    print('your request has been sent successfully.')

                else:
                    time.sleep(0.1)
                    print('failed to send request => You have either entered wrong choice or there is insufficient blood in the storage.')

            else:
                time.sleep(0.1)
                print('Invalid Choice!!!')

        else:
            time.sleep(0.1)
            print('Invalid Password!!!')

    else:
        time.sleep(0.1)
        print('no such donor found!!!')


def view_storage():
    lk=list(bank.keys())
    lv=list(bank.values())
    lp=[]
    for i in range(len(lk)):
        lk[i]='['+lk[i]+']'+str(lv[i])+' ml'
    plt.pie(bank.values(),labels=lk)
    plt.show()
    print('1.Exit')
    val=float(input('Select [1~1]: '))
    if val==1:
        plt.close()
    else:
        print('Invalid Choice!!!')


def become_a_donor():
    time.sleep(0.1)
    new_guy=input('Enter your name: ')
    time.sleep(0.1)
    his_pass=int(input('Create a Pin: '))
    time.sleep(0.1)
    userbase[new_guy]=his_pass
    time.sleep(0.1)
    print('account created successfully!!!')


    


def updater():
    banky=bank
    user=userbase
    requescat=request
    with open('blood_bank_base.py','w') as f:
        f.write('bank='+str(banky)+'\n')
        f.write('userbase='+str(user)+'\n')
        f.write('request='+str(requescat)+'\n')



while True:
    print('*****************************************************************')
    time.sleep(0.1)
    print('*****************************************************************')
    time.sleep(0.1)
    print('****************|~~~~~~~~~~~~~~~~~~~~~~~~~~~~|*******************')
    time.sleep(0.1)
    print('****************|     BLOOD BANK DATABASE    |*******************')
    time.sleep(0.1)
    print('****************|                            |*******************')
    time.sleep(0.1)
    print('****************|1.login as admin            |*******************')
    time.sleep(0.1)
    print('****************|2.login as donor            |*******************')
    time.sleep(0.1)
    print('****************|3.view storage status       |*******************')
    time.sleep(0.1)
    print('****************|4.become a donor            |*******************')
    time.sleep(0.1)
    print('****************|5.Exit                      |*******************')
    time.sleep(0.1)
    print('****************|6.Readme                    |*******************')
    time.sleep(0.1)
    print('****************|                            |*******************')
    time.sleep(0.1)
    print('****************|~~~~~~~~~~~~~~~~~~~~~~~~~~~~|*******************')
    time.sleep(0.1)
    print('*****************************************************************')
    print('*****************************************************************')


    variable=float(input('Select [1~6]: '))
    if variable==1:
        login_as_admin()
    elif variable==2:
        login_as_donor()
    elif variable==3:
        view_storage()
    elif variable==4:
        become_a_donor()
    elif variable==5:
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
        time.sleep(0.1)
        print('|                          Thank you                             |')
        time.sleep(0.1)
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
        time.sleep(0.1)
        break
    elif variable==6:
        time.sleep(0.1)
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
        time.sleep(0.1)
        print('| 1.All the quantities are to be submitted in millilitres.       |')
        time.sleep(0.1)
        print('| 2.Pin should only be in 4 digits.                              |')
        time.sleep(0.1)
        print('| 3.Options should only be selected based on their given number. |')
        time.sleep(0.1)
        print('| 4.Do not create multiple accounts with same name.              |')
        time.sleep(0.1)
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print('1.Exit')
        time.sleep(0.3)
        print('2.about Devs')

        time.sleep(0.1)
        l=int(input('Select :'))
        if l==2:
            time.sleep(0.3)
        
            print('                                                    = ==          ')
            time.sleep(0.3)
            print('                                ========   ==       = ==          ')
            time.sleep(0.3)
            print('                             ===       === == ====                ')
            time.sleep(0.3)
            print('                          ===                                     ')
            time.sleep(0.3)
            print('                        ===         ========                      ')
            time.sleep(0.3)
            print('                       ===       ====        ====                 ')
            time.sleep(0.3)
            print('                     = ===        ====        ====                ')
            time.sleep(0.3)
            print('                   ==   ===         ====       ===                ')
            time.sleep(0.3)
            print('                 ==      ===                =====                 ')
            time.sleep(0.3)
            print('                ======== =  ===          =====                    ')
            time.sleep(0.3)
            print('                               ==========                         ')
            time.sleep(0.3)
            print('                                MADE BY                           ')
            time.sleep(0.3)
            print('                             VIPUL PUROHIT                        ')
            time.sleep(0.3)
            print('                             TUSHAR SHARMA                        ')
            time.sleep(0.3)
            break
    updater()
    





 
                