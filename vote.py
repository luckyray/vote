def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

a = can_vote(20)
print(a)
