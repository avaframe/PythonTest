from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    # ext_modules = cythonize("myMod/myModSub/myCython.pyx"),
    ext_modules = cythonize("myMod/myModSub/dfaCy.pyx",
                          language_level=3),
    include_dirs=[numpy.get_include(), '.']
)


# setup(
#     ext_modules=cythonize("avaframe/com1DFA/DFAfunctionsCython.pyx",
#                           compiler_directives={'linetrace': True},
#                           language_level=3),
# )
