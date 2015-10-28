__author__ = 'MuscioCraft'
DATA = [
    ('Jones', 'Jane', 58),
    ('Smith', 'Anne', 30),
    ('Jones', 'Fred', 30),
    ('Smith', 'John', 60),
    ('Smith', 'Fred', 30),
    ('Jones', 'Anne', 30),
    ('Smith', 'Jane', 58),
    ('Smith', 'Twin2', 3),
    ('Jones', 'John', 60),
    ('Smith', 'Twin1', 3),
    ('Jones', 'Twin1', 3),
    ('Jones', 'Twin2', 3)
]

DATA.sort(key=lambda row: row[1])

for d in DATA:
    print("{:10s} {:10s} {}".format(*d))


