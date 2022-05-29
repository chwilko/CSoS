import os
import numpy as np

_CACHE_FILE = ".MScache_file"
_MSC_USE_CACHE = True


def make_cache_dir(_CACHE_FILE = _CACHE_FILE):
    if not _CACHE_FILE in os.listdir():
        os.mkdir(_CACHE_FILE)


# def get_name(fun, *args):
#     name = ""
#     name += fun.__name__ + "_"
#     for arg in args:
#         name += arg.__name__ + "_"
#     return name


def cache(MSC_name=None):
    if not _CACHE_FILE in os.listdir():
        make_cache_dir(_CACHE_FILE) 
    @use_par(MSC_name)
    def wrapper(MSC_name, fun):
        if MSC_name is None:
            MSC_name = fun.__name__
        def TO_RETURN(*args, use_cache=_MSC_USE_CACHE):
            if MSC_name in os.listdir(_CACHE_FILE) and use_cache:
                return read_from_file(os.sep.join([_CACHE_FILE, MSC_name]))
            ret = fun(*args)
            save_to_file(ret, os.sep.join([_CACHE_FILE, MSC_name]), MSC_name)
            return fun(*args)
        TO_RETURN.__name__ = fun.__name__
        return TO_RETURN
    return wrapper

def save_to_file(lists, file_name, header="", sep_in_data=","):
    ''' NIEPRAWDA DO POPRAWIENIA
    save_to_file(lists, file_name, header="", sep_in_data=",")

    lists -> lista list plików do zapisania
    file_name -> nazwa pliku, w którym mają być zapisane dane
    header -> pierwsza linijka stanowiąca opis danych,
        ignorowana później, przy odczytywaniu
    sep_in_data -> znak jakim mają być oddzielane dane
    Funkcja zapisuje podane estymowane dane do późniejszego wykożystania.
    Aby je późnije odczytać należy użyć funkcji read_from_file.
    '''
    ret = header + "\n"
    for l in lists:
        for i in l:
            ret += str(i) + sep_in_data
        ret = ret[:-1] + "\n"
    try:
        with open(file_name, "w") as f:
            f.write(ret)
    except FileNotFoundError:
        old = os.getcwd()
        path = file_name.split(os.sep)[:-1]
        for i in path:
            os.mkdir(i)
            os.chdir(i)
        os.chdir(old)
        with open(file_name, "w") as f:
            f.write(ret)

def read_from_file(file_name, sep_in_data=",", show_warr=True):
    ''' NIEPRAWDA DO POPRAWIENIA
    read_from_file(file_name, sep_in_data=",", show_warr=True)

    file_name -> nazwa pliku, z którego mają być odczytane dane
    sep_in_data -> znak jakim mają być oddzielane dane
    show_war -> jeżeli true, funkcja wyświetli ostrzerzenie
        jeżeli danych nie uda się zamienić na liczby
        i zwruci je jako str
    Funkcja odczytuje zapisane wczesniej dane funkcją save_to_file.
    '''
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    for i in range(1, len(data)):
        if data[i] == "":
            data = data[:i]
            break
        try:
            data[i] = [float(k) for k in data[i].split(sep_in_data)]
        except:
            data[i] = data[i].split(sep_in_data)
            if show_warr == False:
                continue
            print("Warring! Dane zostały przeczytane jako str.")

    return np.array(data[1:])

def use_par(par):
    '''
    Dekorator, który ustawia w funkji jako pierszy argument,
        argument dekoratora.
    '''
    def MODEL(fun):
        def wrap(*args):
            return fun(par, *args)
        wrap.__name__ = fun.__name__
        return wrap
    return MODEL


if __name__ == "__main__":
    # _MSC_USE_CACHE = False
    @cache("foo")
    def foo(a, b):
        return [[a + b]]
    print(foo(1,2))
    print(foo(1,2))
    print(foo(1,2, use_cache=False))
    print(foo(1,2))

    # get_name()