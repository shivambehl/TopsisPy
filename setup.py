from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='topsispy',
    packages=['topsispy'],
    version='0.0.1',
    license='MIT',
    description='This is a Python Package implementing Topsis used for multi-criteria decision analysis method',
    long_description=readme(),
    long_description_type='text/markdown',
    author='Shivam Behl',
    author_email='shivambehl123@gmail.com',
    url='https://github.com/shivambehl/TopsisPy',
    keywords=['topsis', 'mcda', 'UCS633', 'TIET'],
    install_requires=[
        'numpy',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
    ],
)
