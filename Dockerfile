# Using Python Slim-Buster
FROM biansepang/weebproject:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/THETORNADOTEAM/DEFENDERS-USERBOT /home/DEFENDERS-USERBOT/ \
    && chmod 777 /home/DEFENDERS-USERBOT \
    && mkdir /home/DEFENDERS-USERBOT/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/DEFENDERS-USERBOT/

# Setup Working Directory
WORKDIR /home/DEFENDERS-USERBOT/

# Finalization
CMD ["python3","-m","userbot"]
