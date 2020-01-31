import sys
import os
import re
from setuptools import setup, Command

__PATH__ = os.path.abspath(os.path.dirname(__file__))

def read_readme():
    with open('README.md') as f:
        return f.read()


def read_version():
    # importing gpustat causes an ImportError :-)
    __PATH__ = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(__PATH__, 'mdul/__init__.py')) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")

class DeployCommand(Command):
    description = 'Build and deploy the package to PyPI.'
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass

    @staticmethod
    def status(s):
        print(s)

    def run(self):
        import twine  # we require twine locally  # noqa

        assert 'dev' not in __version__, (
            "Only non-devel versions are allowed. "
            "__version__ == {}".format(__version__))

        with os.popen("git status --short") as fp:
            git_status = fp.read().strip()
            if git_status:
                print("Error: git repository is not clean.\n")
                os.system("git status --short")
                sys.exit(1)

        try:
            from shutil import rmtree
            self.status('Removing previous builds ...')
            rmtree(os.path.join(__PATH__, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution ...')
        os.system('{0} setup.py sdist'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine ...')
        ret = os.system('twine upload dist/*')
        if ret != 0:
            sys.exit(ret)

        self.status('Creating git tags ...')
        os.system('git tag v{0}'.format(__version__))
        os.system('git tag --list')
        sys.exit()

__version__ = read_version()

setup(
    name='mdul',
    version=__version__,
    license='MIT',
    description='An utility to upload local images in markdown to sm.ms and convert markdown file correspondingly.',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/crh19970307/mdul',
    author='Ruiheng Chang',
    author_email='rhchang@pku.edu.cn',
    keywords='markdown image upload convert',
    packages=['mdul'],
    setup_requires=['pytest-runner'],
    tests_require=tests_requires,
    entry_points={
        'console_scripts': ['mdul=mdul:main'],
    },
    cmdclass={
        'deploy': DeployCommand,
    },
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.4',
)










