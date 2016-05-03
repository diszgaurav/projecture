from setuptools import setup
import myproject

def readme():
    with open('README.rst') as f:
        return f.read()
long_description = readme()

setup(name='myproject',
      version=myproject.__version__,
      description='myproject:about',
      long_description=long_description,
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
      ],
      keywords='',
      url='myproject:project_url',
      author='myproject:author_name',
      author_email='myproject:author_email',
      license='MIT',
      packages=['myproject'],
      entry_points = {
          'console_scripts': ['myproject_main=myproject.cmdline:main'],
      },
      tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False)
