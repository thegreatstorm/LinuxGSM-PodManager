FROM centos

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git ansible ncurses sudo
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc
RUN pip3 install pexpect

