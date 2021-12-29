# Looks up member IDs and creates a random new one
# creates a random member ID
import random
def create_member_id():
    test_id = random.randint(0, 99999)
    if member_id_dict.get(test_id) is None:
        return test_id
    else:
        create_member_id()

member_id_dict = {"000001": "admin",
                      "000002": "test"}
