#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
 
"""Convenience wrapper for running gazerr directly from source tree."""
 
from gazerr.cli import main
 
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("---Execution:  %s seconds ---" % (time.time() - start_time))

