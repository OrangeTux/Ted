# Ted

Ted is a set of scripts to read and display data from a cars OBD-II connecter
using an ELM327 adapter. Ted automatically detects which [PID][pid]s are
available and will only query those.

## Installation

Ted is on [PyPI][pypi] and can be installed using [pip][pip].

```bash
$ pip install ted-tools
```

Another option is to install Ted from source:

```bash
$ python setup.py install
```

## Usage

### ted
[ted](scripts/ted) uses the serial interface to a ELM327 adapter to read data
from the OBD-II connector. It publishes this data on a ZeroMQ PUB socket. Other
scripts can subscribe to this socket and can process the data.

The messages published by the ZeroMQ PUB socket follow this format:

```
<mode><pid> <value>
```

The following message contains the current speed of 38 km/h. `01` is the
[mode][mode], `0d` is de PID for the current speed and 38 is the actual value
of this parameter.

```
010d 38
```

```bash
$ ted -h
usage: ted [-h] [-b BAUDRATE] [-d DEVICE] [-p PORT] [-v]

Read OBD-II data using a serial ELM327 interface and publish it on ZeroMQ PUB
socket.

optional arguments:
  -h, --help            show this help message and exit
  -b BAUDRATE, --baudrate BAUDRATE
                        Baudrate to use [default: 38400]
  -d DEVICE, --device DEVICE
                        Path to serial device [default: /dev/ttyUSB0]
  -p PORT, --port PORT  Port to publish data on [default: 1337]
  -v                    Incrase verbosity

```

### tscreen

```bash
$ tscreen -h
usage: tscreen [-h] [-p PORT]

TUI showing currents speed and RPM.

optional arguments:
    -h, --help            show this help message and exit
    -p PORT, --port PORT  Port to read data from [default: 1337]
```

[tscreen](scripts/tscreen) creates a TUI like this:

![tscreenshot](tscreen.png)

## License

Ted is licensed under [Mozilla Public License][mpl].

[mode]: https://en.wikipedia.org/wiki/OBD-II_PIDs#Modes
[mpl]: LICENSE
[pid]: https://en.wikipedia.org/wiki/OBD-II_PIDs
[pip]: https://pip.pypa.io/en/stable/
[pypi]: https://pypi.python.org/pypi/ted-tools
