# Write your tests here. Based on several users' opinion pytest is the right choice: http://pytest.org/latest/

import myproject

#----------------------------------------------------------------------
def test_version():
    assert isinstance(myproject.__version__, float) == True
