FROM python:3
# USER root

COPY ./src /python/src/
WORKDIR /python/src

RUN apt-get update && \
    apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get install -y vim less && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    python -m pip install Flask && \
    python -m pip install jupyterlab && \
    python -m pip install python-dotenv && \
    pip install "line_bot_sdk==1.16.0"


ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8" \
    TZ=Asia/Tokyo \
    TERM=xterm
    # タイムゾーン指定
# ENV TERM xterm # 色数指定
# ENV LANG ja_JP.UTF-8
# ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8
# ENV TZ JST
# ENV TZ=Asia/Tokyo
# ENV TERM xterm


# RUN apt-get install -y vim less && \
#     pip install --upgrade pip && \
#     pip install --upgrade setuptools && \
#     python -m pip install Flask && \
#     python -m pip install jupyterlab && \
#     python -m pip install python-dotenv && \
#     pip install "line_bot_sdk==1.16.0"


# RUN apt-get install -y vim less

# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools


# RUN python -m pip install Flask
# RUN python -m pip install jupyterlab
# RUN python -m pip install python-dotenv

# RUN pip install "line_bot_sdk==1.16.0"

# RUN pip install schedule



# cronの設定　毎日 0時0分にサーバーの稼働状況をLINEで報告
# RUN apt-get install -y cron
# RUN echo '0/* * * * * root python /python/src/main.py' >> /etc/crontab
# # RUN echo '0 0 * * * root python /python/src/main.py' >> /etc/crontab
# # RUN echo '7 1 * * * root python /python/src/main.py' >> /etc/crontab
# CMD ["cron", "-f"]

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# main.go 起動
# CMD ["python", "/python/src/main.py"]
