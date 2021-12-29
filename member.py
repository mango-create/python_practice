from member_id import create_member_id
class member:
    first_name = None
    last_name = None
    id = None

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.id = create_member_id()


class premium_member(member):
    premium = True
    def __init__(self, fn, ln, prem):
        self.premium = prem
        member.__init__(self, fn, ln)
