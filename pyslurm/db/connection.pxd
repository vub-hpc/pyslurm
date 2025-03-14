#########################################################################
# connection.pxd - pyslurm slurmdbd database connection
#########################################################################
# Copyright (C) 2023 Toni Harzendorf <toni.harzendorf@gmail.com>
#
# This file is part of PySlurm
#
# PySlurm is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# PySlurm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# cython: c_string_type=unicode, c_string_encoding=utf8
# cython: language_level=3

from pyslurm cimport slurm
from libc.stdint cimport uint16_t
from pyslurm.slurm cimport (
    slurmdb_connection_get,
    slurmdb_connection_close,
    slurmdb_connection_commit,
)


cdef class Connection:
    """A connection to the slurmdbd.

    Attributes:
        is_open (bool):
            Whether the connection is open or closed.
    """
    cdef:
        void *ptr
        uint16_t flags
