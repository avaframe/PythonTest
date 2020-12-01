"""
Module 1 Main flie
"""

import logging

# create local logger
log = logging.getLogger(__name__)


def Module1Main(cfg):
  """Main function for module 1

  Args:
    foo (int): The foo to bar
    bar (str): Bar to use on foo
    baz (float): Baz to frobnicate

  Returns:
    float: The frobnicated baz
  """

  print('In Module1')
