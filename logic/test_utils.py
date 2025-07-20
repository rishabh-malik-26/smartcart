from logic.utils import remove_punct


def test_remove_punct():
    assert remove_punct("rishabh!!@@''!()-[]}{;:',<>./?@$%^&*_~'''#.,/") == "rishabh"




