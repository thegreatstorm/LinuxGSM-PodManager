FROM centos
ENV container docker
RUN yum -y update; yum clean all
RUN yum -y install systemd; yum clean all; (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); rm -f /lib/systemd/system/multi-user.target.wants/*; rm -f /etc/systemd/system/*.wants/*; rm -f /lib/systemd/system/local-fs.target.wants/*; rm -f /lib/systemd/system/sockets.target.wants/*udev*; rm -f /lib/systemd/system/sockets.target.wants/*initctl*; rm -f /lib/systemd/system/basic.target.wants/*; rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ “/sys/fs/cgroup” ]
CMD [“/usr/sbin/init”]
RUN echo root:test123 | chpasswd

# ssh server
# Don't forget to run '/usr/sbin/sshd -D' if you actually want to ssh into this container
RUN yum install -y openssh-server
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''


EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

RUN systemctl enable sshd
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python38.x86_64 ansible ncurses passwd
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

