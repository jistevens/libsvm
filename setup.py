from setuptools import setup
from distutils.command.build import build as SetuptoolsBuild
from subprocess import call


class MakeBuild(SetuptoolsBuild):
    def run(self):
        call(['make', 'lib'])
        super().run()


setup(
    name='libsvm',
    version='323',
    description='Python package for libsvm',
    packages=['libsvm', 'libsvm.wrapper', 'libsvm.tools'],
    package_dir={'libsvm': '', 'libsvm.wrapper': 'python', 'libsvm.tools': 'tools'},
    package_data={'libsvm': ['libsvm.so.*', 'svm-predict', 'svm-scale', 'svm-train']},
    cmdclass={'build': MakeBuild},
    include_package_data=False,
)

