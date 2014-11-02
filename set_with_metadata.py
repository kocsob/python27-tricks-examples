import datetime

class MyObject:
    def __init__(self, value, meta):
        self.value = value
        self.meta = meta
    def __eq__(self,other):
        return self.value == other.value
    def __hash__(self):
        return hash(self.value)
    def __repr__(self):
        return "%s - %s" % (self.value, self.meta)

def update_metadata_set(set, object):
    try:
        set.remove(object)
    except KeyError:
        pass
    finally:
        set.add(object)

myset = set()
myset.add(MyObject('1', datetime.date(2014, 1, 1)))
myset.add(MyObject('1', datetime.date(2014, 1, 2)))
myset.add(MyObject('2', datetime.date(2014, 1, 3)))
myset.add(MyObject('2', datetime.date(2014, 1, 4)))
myset.add(MyObject('3', datetime.date(2014, 1, 5)))

print myset

update_metadata_set(myset, MyObject('3', datetime.date(2014, 2, 1))) #Update object metadata
update_metadata_set(myset, MyObject('5', datetime.date(2014, 2, 1))) #Add object

print myset