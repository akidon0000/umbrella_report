FROM python:3
# USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools


RUN python -m pip install Flask
RUN python -m pip install jupyterlab
RUN python -m pip install python-dotenv

RUN pip install "line_bot_sdk==1.16.0"

RUN pip install schedule


# RUN apt install -y cron
# COPY cron-example /etc/cron.d/
# RUN chmod 0644 /etc/cron.d/cron-example
# CMD ["cron", "-f"]

RUN apt-get install -y cron
RUN echo '*/1 * * * * root python /python/src/main.py' >> /etc/crontab
# RUN echo '1 0 * * * root python /python/src/main.py' >> /etc/crontab
CMD ["cron", "-f"]
