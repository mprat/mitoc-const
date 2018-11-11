"""
Tests for affiliations.py
"""
import unittest

from mitoc_const import affiliations


class AffiliationsTests(unittest.TestCase):
    """ Test the affiliations constants. """
    def test_affiliation_codes_are_unique(self):
        """ Affiliation codes cannot be repeated. """
        already_seen = set()
        for affiliation in affiliations.ALL:
            self.assertNotIn(affiliation.CODE, already_seen)
            already_seen.add(affiliation.CODE)

    def test_affiliation_codes_are_two_chars(self):
        """ All affiliation codes are two characters. """
        codes = (aff.CODE for aff in affiliations.ALL)
        self.assertTrue(all(len(code) == 2 for code in codes))

    def test_affiliation_values_are_unique(self):
        """ Affiliation values cannot be repeated. """
        already_seen = set()
        for affiliation in affiliations.ALL:
            self.assertNotIn(affiliation.VALUE, already_seen)
            already_seen.add(affiliation.VALUE)

    def test_all_contains_all_affiliations(self):
        """ Ensure that ALL truly contains all defined affiliations. """
        non_deprecated_affiliations = [
            obj for (name, obj) in affiliations.__dict__.items()
            if (isinstance(obj, affiliations.Affiliation) and
                not name.startswith('DEPRECATED'))
        ]
        self.assertEqual(set(non_deprecated_affiliations), set(affiliations.ALL))
