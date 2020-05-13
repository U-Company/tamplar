import fire
from tamplar.api import methods


def main():
    fire.Fire({
        'run': methods.run,
        'kill': methods.kill,
        'init': methods.init,
        'deps': methods.deps,
        'clean': methods.clean(),
    })


if __name__ == '__main__':
    main()
