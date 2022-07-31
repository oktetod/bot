FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b bot https://github.com/oktetod/bot /home/bot/ \
    && chmod 777 /home/bot \
    && mkdir /home/bot/bin/

COPY ./sample_config.env ./config.env* /home/bot/

WORKDIR /home/bot/

CMD ["bash","start"]
