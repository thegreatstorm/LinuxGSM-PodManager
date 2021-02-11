FROM ubuntu:latest

#Setting up pre-requirements.
RUN apt-get update
RUN dpkg --add-architecture i386;
RUN apt update -y ;
RUN apt install -y curl wget file tar bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc jq tmux netcat lib32gcc1 lib32stdc++6 lib32z1
