def test_hello(capsys):
    try:
        import hello
        out, _ = capsys.readouterr()
        assert out == "Hello, world!\n"
    except ModuleNotFoundError:
        assert False, "hello.py not found, check your filename!"

def test_fix_me():
    try:
        from fix_me import age
        assert isinstance(age, int) or isinstance(age, float), "age is not a number!"
    except ModuleNotFoundError:
        assert False, "fix_me.py not found, check your filename!"