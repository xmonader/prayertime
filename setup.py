try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  #  can't have the entry_points option here.

setup(name='prayertime',
      version='2.4',
      author = "Ahmed T. Youssef",
      author_email="xmonader@gmail.com",
      description='prayertimes calculations for Python',
      long_description='calculate prayertimes and qibla direction',
      py_modules=['prayertime'],
      url="http://github.com/xmonader/prayertime",
      license='BSD 3-Clause License',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
       )


