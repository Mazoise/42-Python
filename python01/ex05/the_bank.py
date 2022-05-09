class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):

    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def corrupted_account(self, account):
        attr = dir(account)
        if (len(attr) % 2 == 0
           or any(i[0] is 'b' for i in attr)
           or all("zip" != i[:3:] for i in attr)
           or all("addr" != i[:4:] for i in attr)
           or ("name" not in attr
           and "value" not in attr
           and "id" not in attr)):
            return True
        else:
            return False

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """

        for i in self.account:
            if int(i.id) == origin or str(i.name) == origin:
                origin = i
            if int(i.id) == dest or str(i.name) == dest:
                dest = i
        if (origin not in self.account
           or dest not in self.account
           or origin == dest
           or origin.value < amount
           or amount < 0
           or self.corrupted_account(origin)
           or self.corrupted_account(dest)):
            return False
        else:
            origin.transfer(-amount)
            dest.transfer(amount)
            return True

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        for i in self.account:
            if int(i.id) == account or str(i.name) == account:
                account = i
        attr = dir(account)
        for i in attr:
            if i[0] is 'b':
                delattr(account, i)
        if all("zip" != i[:3:] for i in attr):
            setattr(account, "zip_useless", "")
        if all("addr" != i[:4:] for i in attr):
            setattr(account, "addr_useless", "")
        if ("name" not in attr
           and "value" not in attr
           and "id" not in attr):
            setattr(account, "value", 0.0)
        attr = dir(account)
        if len(attr) % 2 == 0:
            setattr(account, "useless", 0)
        if self.corrupted_account(account):
            return False
        else:
            return True
