# Define the base image
FROM ubuntu:18.04

RUN apt-get update -y \
  && apt-get install -y wget \
  unzip \
  curl \
  aptitude

RUN aptitude install -y libglib2.0-dev

RUN apt-get install -y libnss3 \
  libx11-6 \
  && rm -rf /var/lib/apt/lists/*

#================
# Install Chrome
#================
ARG CHROME_VERSION="google-chrome-beta"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

#============================================
# Chrome webdriver
#============================================
  RUN CHROME_DRIVER_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+(\.[0-9]+){3}).*/\1/") \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && CHROME_DRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROME_DRIVER_VERSION/linux64/chromedriver-linux64.zip" \
  && echo "chromedriver url: "$CHROME_DRIVER_URL \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip $CHROME_DRIVER_URL \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver-linux64/chromedriver /opt/selenium/chromedriver-$CHROME_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_VERSION /usr/bin/chromedriver

# set display port to avoid crash
ENV DISPLAY=:99

# Install required packages
RUN apt-get update \
 && apt-get upgrade\
 && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools

# Copy this repo to a folder in the Docker container
COPY . /project

# Set the work directory
WORKDIR /project

# Install all the required packages
RUN pip3 install -r requirements.txt
