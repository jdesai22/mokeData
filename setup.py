from distutils.core import setup
# import py2exe
# import matplotlib
# import scipy
#
# setup(console=['__main__.py'])


setup(
    name="moke",
    version="1.0.0",
    packages=["data"],
    include_package_data=True,
    install_requires=[
        "matplotlib", "scipy"
    ],
    entry_points={"console_scripts": ["moke=mokeMain.__main__:main"]},
)