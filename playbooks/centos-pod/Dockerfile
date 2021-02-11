FROM centos
# ssh server
# Don't forget to run '/usr/sbin/sshd -D' if you actually want to ssh into this container
RUN yum install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:admin123' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

RUN systemctl enable sshd
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python38.x86_64 ansible ncurses passwd
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

