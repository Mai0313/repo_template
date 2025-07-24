from src.repo_template.cli import hello_fn


def test_hello():
    hello = hello_fn()
    assert hello.name == "Wei"
    assert hello.content == "Hello, World!"
