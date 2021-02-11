FROM ubuntu:latest

#Setting up pre-requirements.
RUN apt-get update
RUN dpkg --add-architecture i386;
RUN apt update -y ;
RUN apt install -y curl wget file tar bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc jq tmux netcat lib32gcc1 lib32stdc++6 lib32z1
ENV TERM=xterm
RUN adduser rustserver --no-create-home --disabled-password --gecos ""
## linuxgsm.sh
RUN wget https://raw.githubusercontent.com/GameServerManagers/LinuxGSM/master/linuxgsm.sh -P /home/rustserver
RUN chmod +x /home/rustserver/linuxgsm.sh
RUN chown rustserver:rustserver -R /home/rustserver/
# USER rustserver
# RUN /home/rustserver/./linuxgsm.sh rustserver
# RUN /home/rustserver/./rustserver install