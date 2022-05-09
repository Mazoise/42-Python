from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Success : The bank transfer failed since the accounts\
     were corrupted')

        bank.fix_account('William John')
        bank.fix_account('Smith Jane')

        if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
            print('Fail : The bank transfer failed even though\
     the accounts should have been fixed')
        else:
            print('Success : The bank transfer was made since\
     the accounts were properly fixed')
    else:
        print('Fail : The bank transfer was made even though\
     the accounts were corrupted')
