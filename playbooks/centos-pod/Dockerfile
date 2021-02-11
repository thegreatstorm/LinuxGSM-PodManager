FROM centos

# ssh server
# Don't forget to run '/usr/sbin/sshd -D' if you actually want to ssh into this container
RUN yum install -y openssh-server
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''
RUN echo root:test123 | chpasswd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

RUN systemctl enable sshd
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python38.x86_64 ansible ncurses passwd
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

