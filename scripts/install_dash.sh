#!/bin/bash
#
py -m pip install dash==0.22.0  # The core dash backend
py -m pip install dash-renderer==0.13.0  # The dash front-end
py -m pip install dash-html-components==0.11.0  # HTML components
py -m pip install dash-core-components==0.26.0  # Supercharged components
py -m pip install plotly --upgrade  # Plotly graphing library used in examples