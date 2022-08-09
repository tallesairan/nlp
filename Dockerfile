FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y sudo

RUN useradd -ms /bin/bash nllb
RUN passwd -d nllb
RUN usermod -aG sudo nllb

COPY bin/init_setup /home/nllb/
RUN chown nllb:nllb /home/nllb/init_setup
RUN chmod 774 /home/nllb/init_setup

# Disable tmux for vast.ai
RUN touch /root/.no_auto_tmux

 