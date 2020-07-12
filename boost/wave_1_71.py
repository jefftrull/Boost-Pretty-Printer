# coding: utf-8

########################################
# Wave 1.71
########################################

# Author: Jeff Trull

from .utils import *

@add_printer
class BoostWaveFlexString:
    """Pretty Printer for Boost.Wave internal string"""
    printer_name = 'boost::wave::util::flex_string'
    min_supported_version = (1, 71, 0)
    max_supported_version = last_supported_boost_version
    template_name = 'boost::wave::util::flex_string'

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return call_object_method(self.val, 'c_str').string()

@add_printer
class BoostWaveFilePosition:
    """Pretty Printer for Boost.Wave File Position"""
    printer_name = 'boost::wave::util::file_position'
    min_supported_version = (1, 71, 0)
    max_supported_version = last_supported_boost_version
    template_name = 'boost::wave::util::file_position'

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return ('(%s %d:%d)' % (str(self.val["file"]), self.val["line"], self.val["column"]))

@add_printer
class BoostWaveToken:
    """Pretty Printer for Boost.Wave CppLexer Token"""
    printer_name = 'boost::wave::cpplexer::lex_token'
    min_supported_version = (1, 71, 0)
    max_supported_version = last_supported_boost_version
    template_name = 'boost::wave::cpplexer::lex_token'

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return '%s : "%s" %s' % (self.val["data"]["id"], self.val["data"]["value"], self.val["data"]["pos"])
