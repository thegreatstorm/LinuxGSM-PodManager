FROM ubuntu:latest

#Setting up pre-requirements.
RUN apt-get update
RUN dpkg --add-architecture i386;
RUN apt update -y ;
RUN apt install -y curl wget file tar bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc jq tmux netcat lib32gcc1 lib32stdc++6 lib32z1
ENV TERM=xterm
RUN adduser rustserver
RUN wget -O /home/rustserver/linuxgsm.sh https://linuxgsm.com/dl/linuxgsm.sh
RUN chmod +x /home/rustserver/linuxgsm.sh
USER rustserver
RUN /home/rustserver/./linuxgsm.sh rustserver
RUN /home/rustserver/./rustserver install