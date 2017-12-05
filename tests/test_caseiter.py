from lambdacookie.caseiter import *


def test_case_iteration():
    assert case_iteration("set-cookie", 0) == "set-cookie"
    assert case_iteration("set-cookie", 1) == "Set-cookie"
    assert case_iteration("set-cookie", 2) == "sEt-cookie"
    assert case_iteration("set-cookie", 3) == "SEt-cookie"
    assert case_iteration("set-cookie", 4) == "seT-cookie"
    assert case_iteration("set-cookie", 5) == "SeT-cookie"
    assert case_iteration("set-cookie", 6) == "sET-cookie"
    assert case_iteration("set-cookie", 7) == "SET-cookie"
    assert case_iteration("set-cookie", 8) == "set-Cookie"
