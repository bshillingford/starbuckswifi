from distutils.core import setup
setup(name='starbuckswifi',
      version='0.1',
      author='Brendan Shillingford',
      description='Simple tool to automate wifi login.',
      scripts=['starbuckswifi.py'],
      py_modules=['starbuckswifi'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
      )


