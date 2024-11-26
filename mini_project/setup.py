from setuptools import setup, find_packages

setup(
    name='himpunan-team6',
    version='0.21.4',
    packages=find_packages(),
    install_requires =[
        #untuk menambhakan requerments tambahan
    ],

    entry_points = {
        "console_scripts" : [
            "HT6 = himpunan_team6:HimpunanTEAM6",
        ],
    },
)

