from Cython.Distutils import build_ext
from distutils.core import setup
from distutils.extension import Extension
import numpy

extensions = [
    Extension('mandelbrot.model.core_cython',
              sources=['mandelbrot/model/core_cython.pyx'],
              include_dirs       = [numpy.get_include()],
              extra_compile_args = ['-fopenmp'],
              extra_link_args    = ['-fopenmp']
    )
]

setup(
    name         = 'mandelbrot',
    version      = '1.0',
    description  = 'Mandelbrot project for Enthought training class',
    author       = 'Enthought Inc.',
    author_email = 'info@enthought.com',
    packages     = ['mandelbrot'],

    ext_modules  = extensions,
    cmdclass     = {'build_ext': build_ext}
)
