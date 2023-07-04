#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    mult = []
    TypeMaList = isinstance(m_a, list)
    TypeMbList = isinstance(m_b, list)
    if not TypeMaList or not TypeMbList:
        raise TypeError("m_a must be a list" if not TypeMaList \
                        else "m_b must be a list")
    for li in m_a:
        if not isinstance(li, list):
            raise TypeError("m_a must be a list of lists")
    for li in m_b:
        if not isinstance(li, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for li in m_a:
        for i in li:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for li in m_b:
        for i in li:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    malen = len(m_a[0])
    mblen = len(m_b[0])
    for row in m_a:
        if malen != len(row):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if mblen != len(row):
            raise TypeError("each row of m_b must be of the same size")
    if malen != mblen:
        raise ValueError("m_a and m_b can't be multiplied")
    for row in m_a:
        rrow = []
        for i in zip(*m_b):
            res = 0
            for j in range(len(row)):
                res += row[j] * i[j]
            rrow.append(res)
        mult.append(rrow)
    return mult
