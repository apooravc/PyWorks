**Sciency**
=====

A package for simple scientific calculations. This package consists of two sub-packages -

1. physy, which provides tools for solving physics problems, for eg - get displacement vector from two given position vectors
2. mathy, which provides mathematical tools used in various situations, for eg - representing vectors and ability to subtract two vectors

**Structure of package**
=====

sciency/
  physy/
    kinematics.py - provides tools for solving kinematics problems
  mathy/
    vector.py - provides tools for various vector operations

**Installation**
=====

For usage, install sciency through following steps -

1. Clone repository through ``git clone https://github.com/apooravc/PyWorks.git``
2. Open command prompt and execute ``pip install -e PyWorks/sciency``

This installs sciency in developer mode so that there's no need to re-install after editing source code. To uninstall use ``pip uninstall sciency``.

**Docs**
=====

Using ``from sciency.mathy import vector``, ``vector`` module provides -

1. ``Vector`` class for representing a vector, usage -

- ``v1 = vector.Vector()`` returns zero vector, i.e., ``0i + 0j + 0k``
- ``v2 = vector.Vector(1,2,3)`` returns vector representing ``1i + 2j + 3k``
- ``v2.getX()`` returns X component of vector ``v2``
- ``v2.getY()`` returns Y component of vector ``v2``
- ``v2.getZ()`` returns Z component of vector ``v2``
- ``v2.print_vector()`` prints vector ``v2`` as ``[1i + 2j + 3k]``
- ``v2.get_magnitude()`` returns magnitude of vector ``v2``
- ``v2.get_unit_vector()`` returns a unit vector in direction of vector ``v2``

2. functions for binary vector operations, usage -

- ``vector.add_vectors(v1, v2)`` returns vector result from ``v1 + v2``
- ``vector.subtract_vectors(v1, v2)`` returns vector result from ``v1 - v2``
- ``vector.get_dot_product(v1, v2)`` returns scalar result from ``v1 . v2``

Using ``from sciency.physy import kinematics``, ``kinematics`` module provides -

1. functions for kinematics operations, usage -

- ``kinematics.get_disp_vector(r1, r2)`` returns (displacement) vector result from ``r1 - r2`` where r1, r2 being position vectors
- ``kinematics.get_avg_vel_vector(disp, t)`` returns (average velocity) vector result from ``disp/t`` where disp, t being displacement vector and time taken respectively
- ``kinematics.get_avg_speed(dist, t)`` returns (average speed) scalar result from ``dist/t`` where dist, t being distance and time taken respectively

**Work to do**
=====

1. Add sub-package chemy, which will provice tools for solving chemistry problems
2. Add more modules under sub-package physy
3. Add more modules under sub-package mathy
4. Add error control
