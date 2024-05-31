FROM alpine

# 安装必要的依赖和 bash
RUN apk update

RUN apk add --no-cache git bash build-base libffi-dev openssl-dev bzip2-dev zlib-dev xz-dev readline-dev sqlite-dev tk-dev linux-headers gcc \
    linux-headers make musl-dev
# Set pyenv home
ARG PYENV_HOME=/root/.pyenv

# Install pyenv, then install python versions
RUN git clone --depth 1 https://github.com/pyenv/pyenv.git $PYENV_HOME && \
    rm -rfv $PYENV_HOME/.git

ENV PATH $PYENV_HOME/shims:$PYENV_HOME/bin:$PATH

# 可选：安装一个特定的 Python 版本
RUN pyenv install 3.7
RUN pyenv local 3.7

# 设置容器启动时执行的命令
CMD ["/bin/bash"]