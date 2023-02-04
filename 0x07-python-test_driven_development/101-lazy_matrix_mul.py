#!/usr/bin/python3
import numpy as np
"""
    The "100-lazy_matrix_mul" module
    This module only has one function: lazy_matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices with numpy"""

    result = np.matmul(m_a, m_b)

    return (result)
