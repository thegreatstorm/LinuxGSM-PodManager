FROM centos

RUN systemctl enable sshd
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python38.x86_64 ansible ncurses passwd
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

# Requirements for LinuxGSM
RUN yum install -y curl wget tar bzip2 gzip unzip python3 binutils bc jq tmux glibc.i686 libstdc++ libstdc++.i686 zlib-devel
