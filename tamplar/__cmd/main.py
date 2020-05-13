import fire
from tamplar.api import methods


def main():
    fire.Fire({
        'run': lambda mode=None, build='yes': methods.run(mode=mode, build=build),
        'kill': lambda: methods.kill(),
        'init': lambda agree=None: methods.init(agree=agree),
        'deps': methods.deps,
        'clean': lambda: methods.clean(),
    })


if __name__ == '__main__':
    main()
