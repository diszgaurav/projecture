from setuptools import setup
import projecture

def readme():
    with open('README.rst') as f:
        return f.read()
long_description = readme()

setup(name='projecture',
      version=projecture.__version__,
      description='scaffolding/bootstrap generation tool',
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Operating System :: POSIX',
      ],
      keywords='project scaffolding',
      url='http://github.com/diszgaurav/projecture',
      author='Gaurav Verma',
      author_email='diszgaurav@gmail.com',
      license='MIT',
      packages=['projecture'],
      tests_require=['pytest'],
      entry_points = {
          'console_scripts': ['projecture_create=projecture.cmdline:main'],
      },
      include_package_data=True,
      zip_safe=False)
