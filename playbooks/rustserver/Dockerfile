FROM centos

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python38.x86_64 ansible ncurses passwd
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

RUN cd /opt/ && git clone https://github.com/thegreatstorm/python-rustserver.git
RUN chmod +x /opt/python-rustserver/rustserver.py
RUN pip3 install -r /opt/python-rustserver/requirements.txt
RUN /opt/python-rustserver/./rustserver.py --install