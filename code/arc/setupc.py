from setuptools import setup, Extension
import numpy

setup(
    ext_modules=[
        Extension(
            "arc_c_extensions",
            ["arc_c_extensions.c"],
            extra_compile_args=['-Wall', '-std=c99', '-O3'],
            include_dirs=[numpy.get_include()]
        )
    ]
)