# Write your tests here. Based on several users' opinion pytest is the right choice: http://pytest.org/latest/

import myproject
import re

#----------------------------------------------------------------------
def test_version():
    m = re.match('^(\d+)\.(\d+)\.(\d+)$', myproject.__version__)
    assert m != None
    assert isinstance(m.groups(), tuple) == True
    for ver in m.groups():
        assert isinstance(int(ver), int) == True
