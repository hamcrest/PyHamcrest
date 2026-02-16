__author__ = "Majority Judgment"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


_locale = "en_US"


def set_locale(new_locale):
    global _locale  # :(|)
    _locale = new_locale


def get_locale():
    global _locale  # :(|)
    return _locale


class LocaleLazyLoader(object):

    # FIXME
    # locales = dict()
    locales = {
        'fr_FR': {
            'Butterfly': 'Papillon',
            'ENGLISH DESCRIPTION': 'DESCRIPTION FRANÇAISE',

            'Assertion failed': "Échec d'une assertion",
            'Expected: ': 'Attendu⋅e: ',
            '     but: ': '     mais: ',
            'was ': "obtenu⋅e ",
        },
    }

    def get_locale_map(self, locale):
        if locale not in self.locales:
            self.locales[locale] = dict()
        return self.locales[locale]


locale_loader = LocaleLazyLoader()
