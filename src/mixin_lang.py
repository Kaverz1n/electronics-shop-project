class MixinLang():
    '''
    Класс-Миксин, отвечащий за смену
    языка
    '''
    LANGUAGES = ['EN', 'RU']
    IS_ENG = True

    def __init__(self):
        self._language = MixinLang.LANGUAGES[0]

    def change_lang(self):
        '''
        Меняет язык раскладки
        на следующий в списке
        доступных языков.
        '''
        if MixinLang.IS_ENG:
            self._language = MixinLang.LANGUAGES[1]
            MixinLang.IS_ENG = False
            return self
        else:
            self._language = MixinLang.LANGUAGES[0]
            MixinLang.IS_ENG = True
            return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError('Менять значение можно лишь через функцию change_lang()')
