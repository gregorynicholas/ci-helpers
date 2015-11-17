import os

# The test scripts accept 'stable' for ASTROPY_VERSION to test that it's
# properly parsed hard-wire the latest stable branch version here

LATEST_ASTROPY_STABLE = '1.0'

if os.environ.get('PIP_DEPENDENCIES', None) is not None:
    PIP_DEPENDENCIES = os.environ['PIP_DEPENDENCIES'].split(' ')
else:
    PIP_DEPENDENCIES = []

if os.environ.get('CONDA_DEPENDENCIES', None) is not None:
    CONDA_DEPENDENCIES = os.environ['CONDA_DEPENDENCIES'].split(' ')
else:
    CONDA_DEPENDENCIES = []

dependency_list = PIP_DEPENDENCIES + CONDA_DEPENDENCIES


def test_numpy():
    if os.environ.get('NUMPY_VERSION', None) is not None:
        import numpy
        try:
            assert numpy.__version__.startswith(os.environ['NUMPY_VERSION'])
        except AssertionError:
            assert 'dev' in numpy.__version__


def test_astropy():
    if os.environ.get('ASTROPY_VERSION', None) is not None:
        import astropy
        try:
            assert astropy.__version__.startswith(os.environ['ASTROPY_VERSION'])
        except AssertionError:
            if os.environ['ASTROPY_VERSION'] == 'stable':
                assert astropy.__version__.startswith(LATEST_ASTROPY_STABLE)
            else:
                assert 'dev' in astropy.__version__


# Check whether everything is installed and importable
def test_dependency_imports():
    for package in dependency_list:
        __import__(package)
