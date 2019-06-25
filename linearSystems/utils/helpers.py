"""
    Holds shared Control functions
"""
import control as ct


def get_sys(system, sys_name='series'):
    """
        Combines a TF denominator and nume to a single TF
        expression
    """
    try:
        res = getattr(ct, sys_name)(system[0], system[1])
    except (IndexError, TypeError):
        return getattr(ct, sys_name)(system)
    else:
        return res
