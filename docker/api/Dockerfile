FROM python:3.7.6


ENV PYTHONPATH=/app/api
EXPOSE ${PORT:-5000}
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN pip install --upgrade pip

COPY ./api /app/api
COPY ./docker /app/docker
COPY ./scripts /app/scripts

WORKDIR /app

ARG requirements=/app/docker/api/requirements/prd.txt
RUN pip install -r ${requirements}

CMD ["/app/scripts/start.sh"]
