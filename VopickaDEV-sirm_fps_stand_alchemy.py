#! /usr/bin/env python3

# region - Dependencies
try:
    errstat = False
    __dependencies__ = []

    trying = "logging"
    __dependencies__.append(trying)
    import logging

    trying = "sys"
    __dependencies__.append(trying)
    import sys

    assert sys.version_info >= (
        3,
        6,
    ), f"Incorrect Python version -- {sys.version_info} -- must be at least 3.6"

    trying = "os"
    __dependencies__.append(trying)
    import os

    os.chdir(os.path.dirname(__file__))

    trying = "datetime.datetime"
    __dependencies__.append(trying)
    from datetime import datetime

    # TODO - Add requirements

except ImportError:
    errstat = True
finally:
    # DOC - Configure the logging system
    logging.basicConfig(
        filename=f"{sys.argv[0].replace('.py', '')}-{datetime.now().strftime('%Y_%m_%d-%H_%M_%S')}.log.log",
        format="%(asctime)s-[%(levelname)s]-(%(filename)s)-<%(funcName)s>-#%(lineno)d#-%(message)s",
        datefmt="%Y.%m.%d %H:%M:%S",
        filemode="w",
        level=logging.WARNING,
    )

    # REM - Configure a named logger to NOT use the root log
    logger = logging.getLogger(sys.argv[0].replace(".py", ""))
    logger.setLevel(logging.DEBUG)

    # REM - Configure and add console logging to the named logger
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(asctime)s-[%(levelname)s]-%(message)s"))
    logger.addHandler(console)

    if errstat is True:
        logger.fatal(f"Find missing library! -->{trying}<--")
        raise SystemExit(f"Find missing library! -->{trying}<--")

    # REM - Clean up
    del trying
    del errstat
# endregion - Dependencies

# region Header Block #########################################################
__project__ = sys.argv[0]
__purpose__ = "Merge and split stands for reporting or depletion"
__license__ = "BSD3"
__maintainer__ = "Charles E. Vopicka"
__email__ = "chuck@vopicka.dev"
# __status__ = "Prototype"
# __status__ = "Development"
# __status__ = "Production"
__status__ = "Prototype"
__revisionhistory__ = [
    ["Date", "Type", "Author", "Comment"],
    ["2023.12.20", "Created", __maintainer__, "Script Created"],
]
__created__ = __revisionhistory__[1][0]
__author__ = __revisionhistory__[1][2]
__version__ = __revisionhistory__[len(__revisionhistory__) - 1][0]
if __created__.split(".")[0] != __version__.split(".")[0]:
    __copyright__ = f'Copyright {__created__.split(".")[0]} - {__version__.split(".")[0]}, {__maintainer__}'
else:
    __copyright__ = f'Copyright {__created__.split(".")[0]}, {__maintainer__}'
__copyrightstr__ = "This program comes with ABSOLUTELY NO WARRANTY;\n\n"
__copyrightstr__ += "This is free software, and you are welcome to redistribute it under certain conditions;"
__credits__ = []
for n, x in enumerate(__revisionhistory__):
    if x[2] not in __credits__ and n > 0:
        __credits__.append(x[2])

logger.info(
    "\n".join(
        (
            "\n",
            __purpose__,
            f"\nBy:\t{__author__}",
            f"\t{__email__}",
            "",
            f"License:\t{__license__}",
            "",
            __copyright__,
            "",
            __copyrightstr__,
            f"\nCreated:\t{__created__}",
            f"Version:\t{__version__} ({__status__})",
            f"Rev:\t\t{len(__revisionhistory__) - 1}",
            "",
        )
    )
)
# endregion Header Block ######################################################


# region - Functions here
def MyFunction(variable):
    pass


# endregion - End of functions


if __name__ == "__main__":

    MyFunction("Values")
