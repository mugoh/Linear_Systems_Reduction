"""
    FeedBack [Non-Unity]
"""

from .example1 import serify

from ..utils.display import td

import control as ct


def non_unity_feedback():
    """
        Gets the transfer function from a feedback system
    """
    # Get sys1 and sys2 transfer functions from series
    sys_g, sysh = serify(called=True)

    sys_feedback_tf = ct.feedback(sys_g, sysh, sign=-1)

    td.ouput('Non Unity Feedback Series TF', keys=['G(c)', 'G(s)', 'sys tf'],
             values=[sysh, sys_g, sys_feedback_tf])
