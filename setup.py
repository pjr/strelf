from setuptools import setup, find_packages

setup(
    name='strelf',
    author='Philip Reynolds',
    email='phil@growlabs.io',
    keywords='stripe, migrate, account, elf',
    version='0.1',
    python_requires=">=3.7",
    install_requires=['click', 'stripe', 'python-dotenv'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'strelf = strelf.cli:cli'
        ]
    }
)
