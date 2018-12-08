# Docker file for Bank Marketing Analysis
# Brenden Everitt and Sabrina Tse, December 2018

# Use rocker/tidyverse as the base image
FROM rocker/tidyverse

# then install the python and its dependencies
# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# get python package dependencies
RUN apt-get install -y python3-tk

# install numpy, pandas & matplotlib
RUN sudo apt-get install -y graphviz
RUN pip3 install graphviz
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install seaborn
RUN pip3 install sklearn
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*
