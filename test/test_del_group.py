from model.group import Group
import random

#def test_delete_all_groups(app):
#    app.group.delete_all_groups()


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    old_groups = db.get_group_list()
#    index = random.randrange(len(old_groups))
    group = random.choice(old_groups)
#    app.group.delete_group_by_index(index)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
#    old_groups[index:index+1] = []
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

