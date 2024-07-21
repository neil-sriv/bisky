FROM ubuntu:22.04 as server

RUN apt-get update -y
RUN apt-get install curl -y -V
RUN apt-get update && apt-get install -y lsb-release && apt-get clean all

RUN curl https://raw.githubusercontent.com/bluesky-social/pds/main/installer.sh >installer.sh
RUN chmod +x installer.sh
# RUN ./installer.sh
