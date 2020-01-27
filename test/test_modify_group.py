from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="NewGroupName"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="NewGroupHeader"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="testGroupFooter"))
