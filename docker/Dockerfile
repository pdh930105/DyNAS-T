ARG BASE_VERSION=22.12
FROM nvcr.io/nvidia/pytorch:${BASE_VERSION}-py3 as base

ENV DEBIAN_FRONTEND noninteractive

ARG USER_ID
ARG GROUP_ID
ARG USER_NAME
RUN apt-get clean
RUN rm -rf /var/atp/lists/*
# this line change to ubuntu archive
RUN apt-get update -y
RUN apt-get install vim -y
RUN apt-get install tmux -y
RUN apt-get install sudo -y

RUN addgroup --gid $GROUP_ID $USER_NAME
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER_NAME
RUN echo ${USER_NAME}:${USER_NAME}|chpasswd
RUN adduser pdh sudo
RUN echo ${USER_NAME} 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# python library install
RUN pip install timm
RUN pip install yacs
RUN pip install pyhocon
RUN pip install -U fvcore
RUN pip install -U pymoo
RUN pip install -U ofa==0.1.0.post202203231606
RUN pip install -U PyYAML
RUN pip install -U torchprofile

USER ${USER_NAME}
WORKDIR /home/${USER_NAME}

ENTRYPOINT ["/opt/nvidia/nvidia_entrypoint.sh"]

