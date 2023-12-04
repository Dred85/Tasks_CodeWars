def who_is_paying(name):
    """"Работаем со списком: выводим name и обрезаем name до 2 символов, если len(name) > 2"""
    return [name, name[:2]] if len(name) > 2 else [name]




print(who_is_paying("Mede"))