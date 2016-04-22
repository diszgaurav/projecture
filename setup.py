from setuptools import setup
import projecture

def readme():
    with open('README.rst') as f:
        return f.read()
long_description = readme()

setup(name='projecture',
      version=projecture.__version__,
      description='scaffolding/bootstrap collection',
      long_description=long_description,
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
      ],
      keywords='',
      url='http://github.com/diszgaurav/projecture',
      author='Gaurav Verma',
      author_email='diszgaurav@gmail.com',
      license='MIT',
      packages=['projecture'],
      tests_require=['pytest'],
      scripts=[],
      include_package_data=True,
      zip_safe=False)
