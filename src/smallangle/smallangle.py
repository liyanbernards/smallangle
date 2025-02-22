import click
import numpy as np
from numpy import pi
import pandas as pd


# command group for sin & tan functions
@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.argument("number", type=int)
def sin(number):
    """calculate sin values in range 0-2pi.

    Args:
        number (int): number of x values in range
    """

    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.argument("number", type=int)
def tan(number):
    """calculate tan values in range 0-2pi.

    Args:
        number (int): number of x values in range
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()
