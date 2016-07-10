import uuid
import py.test
from sqlobject import *
from sqlobject.tests.dbtest import *


########################################
# Uuid columns
########################################


testuuid = uuid.UUID('7e3b5c1e-3402-4b10-a3c6-8ee6dbac7d1a')

class UuidContainer(SQLObject):
    uuiddata = UuidCol(default=None)


def test_uuidCol():
    setupClass([UuidContainer], force=True)

    my_uuid = UuidContainer(uuiddata=testuuid)
    iid = my_uuid.id

    UuidContainer._connection.cache.clear()

    my_uuid_2 = UuidContainer.get(iid)

    assert my_uuid_2.uuiddata == testuuid
