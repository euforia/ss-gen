========================
Startup Script Generator
========================

This tool generates basic startup scripts for RHEL based linux distributions with the provided options.

Usage
-----
::
ss-gen.py [options]

Options:
  -h, --help            show this help message and exit
  --name=NAME
  --path=BINARY_PATH    Path to binary
  --args=BINARY_ARGS    Arguments to executable
  --description=DESCRIPTION
  --run-levels=RUN_LEVELS
                        Run levels
  --start-order=START_ORDER
                        Start order
  --stop-order=STOP_ORDER
                        Shutdown order
