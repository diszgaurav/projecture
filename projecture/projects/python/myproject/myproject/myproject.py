"""myproject
"""
__author__ = 'myproject:author_name'
__email__ = 'myproject:author_email'

#----------------------------------------------------------------------
def hello_world(extend_hello=False):
    """prints hello world

    :returns: None
    :rtype: None

    """

    print 'Hello World!{}'.format(' Beautiful World!' if extend_hello else '')
