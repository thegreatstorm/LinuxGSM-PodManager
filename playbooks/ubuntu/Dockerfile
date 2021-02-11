FROM ubuntu:latest
# Setting up SteamCMD install
RUN dpkg add --update --no-cache \
        tar \
        wget \
 && mkdir -p /app \
 && wget --no-verbose 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' -O '/tmp/steamcmd_linux.tar.gz' \
 && tar -C /app -xf '/tmp/steamcmd_linux.tar.gz' \
 && ln -s steamcmd.sh /app/steamcmd

#Setting up pre-requirements.
RUN apt-get update
RUN dpkg --add-architecture i386;
RUN apt update -y ;
RUN apt install -y curl wget file tar bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc jq tmux netcat lib32gcc1 lib32stdc++6 lib32z1 steamcmd

# Getting steamcmd as environment variable.
ENV DEBIAN_FRONTEND=noninteractive \
    PATH=$PATH:/opt/steamcmd
COPY --from=base /app /opt/steamcmd
RUN chmod -R a=u /opt/steamcmd
WORKDIR /opt/steamcmd
ENTRYPOINT ["steamcmd"]
ONBUILD ENTRYPOINT []