FROM python:3.9-alpine

#Make sure that any Python output is sent straight to the terminal
ENV PYTHONBUFFERED=1
ENV PATH="/scripts:${PATH}"

RUN adduser -D user

#Set working directory and source the bin file
WORKDIR /home/user/shopping_list
ENV PATH $PATH:/home/user/.local/bin

COPY --chown=user:user ./shopping_list /shopping_list
COPY --chown=user:user ./scripts /scripts
COPY --chown=user:user manage.py /shopping_list

#copy local project requirements file to containing image
COPY --chown=user:user ./requirements.txt /requirements.txt

#Install dependencies
USER root
RUN apk add --update gcc libc-dev linux-headers postgresql-dev musl-dev

USER user
RUN pip install -r /requirements.txt

RUN chmod +x /scripts/*

ENTRYPOINT "entrypoint.sh"
