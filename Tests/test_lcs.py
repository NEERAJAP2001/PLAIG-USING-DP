# Essential imports 
import back
import pytest

# inital tests
def test_lcs():
    assert back.lcs("AGGTAB","GXTXAYB") == 4
    assert back.lcs('hello','hello') == 5
    assert back.lcs('','') == 0 


# test with few more cases
def test_lcs_para():
    assert back.lcs("Hey Whats up?","Hey Hello?") == 5
    assert back.lcs('122','12') == 2
    assert back.lcs('_*&^','_^&%') == 2
