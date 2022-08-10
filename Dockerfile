FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y sudo zip git wget curl nano screen htop tzdata build-essential
RUN useradd -ms /bin/bash nlp
RUN passwd -d nlp
RUN usermod -aG sudo nlp
COPY bin/init_setup /home/nlp/
RUN mkdir /home/nlp/utils
RUN chown nlp:nlp /home/nlp/init_setup
RUN chmod 774 /home/nlp/init_setup
# Disable tmux for vast.ai
RUN touch /root/.no_auto_tmux
ENV CUDA_VISIBLE_DEVICES=0,1