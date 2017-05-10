import linkcheck_helper
import numpy.testing as npt
import requests
import unittest

test = {}

servers = ["http://127.0.0.1:8000/","https://qedinternal.epa.gov/"]

pages = [""]

pages_to_test = [s + p for s in servers for p in pages]

class TestQEDHost(unittest.TestCase):
    """
    this testing routine accepts a list of servers where a group of models and pages (i.e.,tabs)
    are presented as web pages.  it is assumed that the complete set of models and related pages
    are present on each server. this routine performs a series of unit tests that ensure
    that the web pages are up and operational.
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    @staticmethod
    def test_qed_200():
        test_name = "Splash page access"
        try:
            assert_error = False
            response = [requests.get(p).status_code for p in pages_to_test]
            try:
                npt.assert_array_equal(response, 200, '200 error', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, pages_to_test, response)
        return


