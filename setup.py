from setuptools import setup

setup(
    name='pyxel_app',
    version='0.1',
    py_modules=['pyxel_app'],
    install_requires=[
        'Click',
        'pyxel',
    ],
    entry_points='''
        [console_scripts]
        pyxel_app=pyxel_app:pyxel_app
    ''',
)