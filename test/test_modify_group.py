from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = app.group.get_group_list()
    group = Group(name="NewGroupName")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = "test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="NewGroupHeader"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name = "test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="testGroupFooter"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
