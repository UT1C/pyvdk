import logging as log


log.basicConfig(
    format='%(asctime)s [%(levelname)s] (%(name)s) %(message)s',
    datefmt='%d.%m.%y %H:%M:%S',
    level=log.INFO
)


def toggle_debug():
    """ Toggle debug mode """

    log.root.setLevel(log.DEBUG)