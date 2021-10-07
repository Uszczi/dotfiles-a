from setuptools import setup

setup(
    name="dotfiles-app",
    version="0.1",
    py_modules=["df"],
    entry_points="""
        [console_scripts]
        dotfiles=df.cli:cli
    """,
)
