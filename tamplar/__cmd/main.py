import fire
from tamplar.api import methods


def main():
    fire.Fire({
        'init': lambda agree=None: methods.init(agree=agree),
        'deps': methods.deps,
        'clean': methods.clean,
    })


if __name__ == '__main__':
    main()
