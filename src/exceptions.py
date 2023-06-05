class InstantiateCSVError(Exception):
    '''
    Исключения повреждения CSV-файла
    '''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'
