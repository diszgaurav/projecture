import projecture

def test_list_projects():
    lp = projecture.list_projects()
    assert True == isinstance(lp, list)
