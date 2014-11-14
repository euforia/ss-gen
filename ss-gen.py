#!/usr/bin/env python

import os
import sys
from optparse import OptionParser

TEMPLATE = "startup-script.template"

def init_options():
    parser = OptionParser()
    parser.add_option("--name",        dest="name")
    parser.add_option("--path",        dest="binary_path",               help="Path to binary")
    parser.add_option("--args",        dest="binary_args", default="",   help="Arguments to executable")
    parser.add_option("--description", dest="description", default="")
    parser.add_option("--run-levels",  dest="run_levels",  default=2345, type="int", help="Run levels")
    parser.add_option("--start-order", dest="start_order", default=90,   type="int", help="Start order")
    parser.add_option("--stop-order",  dest="stop_order",  default=10,   type="int", help="Shutdown order")
    (opts, args) = parser.parse_args()

    if not opts.binary_path:
        print "\nBinary path required!\n"
        parser.print_help()
        sys.exit(1)

    if not opts.name:
        opts.name = os.path.basename(opts.binary_path)

    return opts, args


def apply_template(data):
    fh = open(TEMPLATE, "rb")
    template_data = fh.read()
    fh.close()
    return template_data %(data)

def write_template(data):
    tmp_data = apply_template(data)
    fh = open(data["name"], "wb")
    fh.write(tmp_data)
    fh.close()
    print "Startup script generated: ./%(name)s" %(data)

def main():
    (opts, args) = init_options()
    try:
        input_data = {
            "binary"     : opts.binary_path,
            "options"    : opts.binary_args,
            "run_levels" : opts.run_levels,
            "start_order": opts.start_order,
            "stop_order" : opts.stop_order,
            "name"       : opts.name,
            "description": opts.description
        }
        write_template(input_data)
        return 0
    except Exception, e:
        print e
        return 1

if __name__ == "__main__":
    sys.exit(main())
