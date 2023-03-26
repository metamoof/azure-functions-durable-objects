import nox

PYTHONVERSIONS = [
    "3.7",
    "3.8",
    "3.9",
    "3.10",
]


@nox.session(python=PYTHONVERSIONS)
def tests(session):
    # same as pip install -r -requirements.txt
    session.install("-r", "requirements.txt")
    session.install("pytest")
    session.run("pytest", "-v", "tests")


@nox.session(python=PYTHONVERSIONS)
def lint(session):
    session.install("flake8")
    session.install("flake8-docstrings")
    session.run("flake8", "./durable_objects/")


@nox.session(python=PYTHONVERSIONS)
def typecheck(session):
    session.install("-r", "requirements.txt")
    session.install("mypy")
    session.run("mypy", "./durable_objects/")


@nox.session(python=PYTHONVERSIONS)
def autopep(session):
    session.install("-r", "requirements.txt")
    session.run(
        "autopep8",
        '--in-place --aggressive --aggressive --recursive "./durable_objects/"',
    )
